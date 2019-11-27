# Project Name

## Goals
To have a way to specify the name a project is listed under in an index.

## Comparisons

### Flit
Has a
[`dist-name` field](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section).

When the import name matches the project name, the
[`module` field](https://flit.readthedocs.io/en/latest/pyproject_toml.html)
which also specifies the code to include in a wheel is used automatically.

### Setuptools
Has a
[`name` field](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata).
There isn't an included way to infer the name from the package/module name.

### Poetry
Has a [`name` field](https://poetry.eustace.io/docs/pyproject/#name).

This field also provides a default package name to figure out what code to put
into a wheel.

### Rust
Has a [`name` field](https://doc.rust-lang.org/cargo/reference/manifest.html#the-name-field).

Acts as the default name to infer the build names.

### npm
Has a [`name` field](https://docs.npmjs.com/files/package.json#name).
There isn't any inference of what code to include.

## Conclusions
* Every tool has a way to manually specify the project's name
* _Nearly_ every tool has a `name` field (Flit is the only difference with `dist-name`)
* 3 of the tools provide a mechanism to use a name/module specification to
  infer the other
  - Flit is the only one where the specification of what code to include infers
    the name instead of vice-versa
