# Version

This document is a little different from others. There really isn’t much interesting about declaring a version, and the string format is already well-documented in [PEP 440](https://www.python.org/dev/peps/pep-0440/). Instead, we discuss here about how tools *use* the version declaration.

## Goals

Specify a package version that can be used by package managers at install time, and inspected after the installation (e.g. to decide whether an upgrade is needed).

 The package should also be able to read out the value at runtime.

## Comparisons

### Setuptools (vanilla)

Setuptools only concerns itself with metadata, the version passed in for the `setup()` is only transfered into the package metadata. Making it availiable as a variable is expected to be solved by the maintainer.

It is generally suggested to query the package metadata for the version to ensure a single source of truth. Commonly `pkg_resources` or `importlib_metadata` are suggested tools to facilitate this transfer.

#### Advantages

Singles source of truth.

#### Disadvantages

The usage of the python metadataa system requires adequate packaging and usage of runtime dependencies, this is not always desirable.
When wanting to use Direct metadata, the version number needs to be maintained in multiple places.


### Setuptools: `setuptools_scm`

Reads the version from SCM to `setup.py` at build time. This does not really fit with the rest, but probably should be mentioned.

```python
from setuptools import setup
setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
```
or
```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=42", "wheel", "setuptools_scm[toml]>=3.4"]
[tools.setuptools_scm]
write_to = "src/myproject/_version.py"
```
#### Advantages

Has the unique ability to keep the SCM and package metadata in sync, which non of the rest entries could IIUC.
Can create and update direct metadata.

#### Disadvantages

Couples Version metadata with SCM metadata, which is problematic in certain packaging setups.

### Setuptools: `setup.py` imports the package at build time

```python
import mypackage
setup(version=mypackage.__version__)
```

Setuptools also offers a `version = attr:` shorthand to do the same thing declaratively in `setup.cfg`.

#### Advantages

Probably the most straightforward way to satisfy the requirements.

The package can use the value without relying on the package manager.

#### Disadvantages

The package needs to be importable at install-time, i.e. *before it is actually installed*. In general this is achieved by ultilising the fact (exploiting an implementation quirk?)  that the current working directory is in `sys.path` when `setup.py` is run.

Makes it impossible to inspect a package’s version without first building it, posing a problem for the package manager. This can be circumvented by carefully structuring the package.

### Setuptools: `setup.py` parses a file without importing

```python
# src/mypackage/_version.py
__version__ = '1.2.3'

# src/mypackage/__init__.py
from ._version import __version__

# setup.py
version = (
    pathlib.Path('src/mypackage/_version.py')
    .read_text()
    .split('=', 1)
    [-1]
    .strip()
)
setup(version=version)
```

Alternative approaches include using `ast.literal_eval()`, using a plain text file, parsing `__init__.py` directly, etc.

#### Advantages

Relatively straightforward, but avoids the biggest problems of importing.

Note that while a package’s ability to be imported is not guarenteed, its path relative to `setup.py` is.

The package can use the value without relying on the package manager.

Works well with the PyPA-recommended<sup>[*citation needed*]</sup> `src` structure (a side effect of the import method’s exploiting `sys.path`).

#### Disadvanteges

Requires significant concern to structure the package properly. If you use a plain text file, better remember to include it in `package_data`. If you parse a Python file literally, better be sure not to mess up the source.

Maybe pedantic: While the source is indeed there, is there guarentee it’s *readable*?

### Flit

A similar approach to the import method of Setuptools, but always and only reads `__version__` in the package’s top level import. This means that:

*  There is formal `sys.path` support in the build tool, plus automatic `src/` discovery.

* Little choice in project structuring. Advantage or disadvantage?

And as the import method above:

* Advantage: The package can use the value without relying on the package manager.

* Disadvantage: It is still difficult for a package manager to inspect the version from package source, with slightly different caveats from Setuptools.

### Poetry

Uses a `version` field to specify the version in `pyproject.toml`. No effort to make it available in code.

All advantages and disadvantages are the same as vanilla Setuptools.

### NPM and Yarn

Uses a `version` field to specify the version in metadata.

All advantages and disadvantages are the same as vanilla Setuptools, but with one twist—

The `node_modules` structure allows the code to read `package.json` at runtime, so a reverse variant of the import method is possible:

```js
const {version} = require('./package.json')
```

Since it is the package importing metadata, the same import-before-install problem does not apply.

On the other hand, you’d need to remember to distribute `package.json` with the source if you decide to vendor or re-package the code. This is especially a problem for browsification, since explosing `package.json` to the client has [security implications](https://stackoverflow.com/a/10855054).

### Cargo

Uses a `version` field to specify the version in metadata.

The code is expected to use `env!("CARGO_PKG_VERSION")` to retrieve the version string. This macro is expanded at build time into the actual version string.

This is probably the most complete package I’ve seen. Yes, it ties compilation to Cargo, but the coupling is loose enough you can still manually pass the version to the compiler if you need to. The compiler is also smart to emit a helpful (enough) message if you do not pass it.

Of course, this approach is not completely viable for Python, since Rust crates are always compiled (so you don’t have the same vendoring issue), but if we can take inspiration from it, it’s **duplication might not be the problem, but we need to provide a good way to keep the duplicated entries in sync**.


