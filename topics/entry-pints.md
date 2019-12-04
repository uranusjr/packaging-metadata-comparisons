# Entry Points

## Goals

To have a way to let the user, after installing the package, can invoke a certain function in it without necessarily knowing where and how the function is declared or implemented.

The most common form of this functionality are command scripts. A command script declaration would create an executable on install time, which invokes the specified function in the specified environment when executed.

For Python packages, entry points are declared in the `entry_points.txt` file inside the wheel’s `.dist-info` database. This is an INI file.<sup>*[citation needed]*</sup> Each section represents an entry point group, which acts to categorise what an entry point is for. Group naming is almost free-form, with only two reserved special names: `console_scripts` and `gui_scripts`, which are used to declare scripts. (The latter on Windows creates scripts run by `pythonw.exe` instead of `python.exe`.)

Each entry point is declared as:

```ini
command = path.to.module:callable
```

## Non-goals

Since this document is about packaging, it will not discuss *project* scripts, i.e. alias-like declarations to let a project developer invoke certain command easily, e.g. package.json’s `scripts` field.

## Comparisons

### Setuptools

There are several equivalent ways to declare it, all using the same structure as the resulting INI. The most common way is to pass a dict to the `entry_points` dict in setup.py:

```python
setup(
    entry_points={
        "console_scripts": {
            "command": "path.to.module:callable",
        },
        "mypackage.customgroup": {
            "foo": "mypackage.plugins:foo",
        },
    },
)
```

There is also a `scripts` field that accepts a list of paths pointing to concrete script files, but this is generally considered a niche feature. The end result is also slightly different from most people consider command scripts because those files are not guarenteed to be executable.

### Flit

There is an `entrypoints` section in the same format (but in TOML):

```toml
[tool.flit.entrypoints."mypackage.customgroup"]
foo = "mypackage.plugins:foo"
```

There is also a `scripts` section. Contents are converted into `console_scripts` entries:

```toml
[tool.flit.scripts]
command = "path.to.module:callable"
```

It is not clear whether the user can declare console scripts in the `entrypoints` section.

### Poetry

Entry points are defined in the `plugins` section:

```toml
[tool.poetry.plugins."mypackage.customgroup"]
foo = "mypackage.plugins:foo"
```

There is a `scripts` section. Contents are converted into `console_scripts` entries:

```toml
[tool.poetry.scripts]
command = "path.to.module:callable"
```

It is not clear whether the user can declare console scripts in the `plugins` section.

### Cargo

Only has console (and GUI) scripts equivalents. Other entry point functionalities are not possible anyway since Rust does not support dynamic linking right now.

Instead of treating a command script as a “proxy” to the underlying library, Cargo gives commands the same status as libraries. A top-level module must be explicitly declared as either a command or a library. It is possible for a crate (Cargo’s equivalent of a package distribution) to contain both commands and libraries, and a command can rely on libraries in the same crate, but those are implemention choices made by the developer, not imposed by package metadata.

```toml
[[bin]]
name = "command"
path = "./src/main.rs"

[[lib]]
name = "mypackage"
path = "./src/lib.rs"
```

```rust
// ./src/main.rs
extern crate mypackage;
fn main() { mypackage::callable(); }
```

```rust
// ./src/lib.rs
pub fn callable() {}
```

### `packages.json`

The equivalent of console scripts are declared under the `bin` object.*[see notes]* Each key is the command name, and value is (relative) path to a JavaScript file. npm (and Yarn) automatically generates an executable wrapping the file on install time. Therer are no other entry point functionalities.

```json
{
  "bin": {
    "command": "./cli.js"
  }
}
```

```js
// ./cli.js
var mypackage = require('./src/index.js')
mypackage.callable()
```

```js
// ./src/index.js
function callable() {}
export default {callable: callable}
```

This approach is conceptually similar to Cargo’s, but the declaration is less prominent. The `bin` entry feels more like an add-on to the “main” library declaration, rather than on the same level like Cargo’s `[bin]` vs `[lib]`.

*Note:* As typical JavaScript fashion, there are shortcut notations, but they all mean the same thing, and Python people probably are not interested in such complications anyway.
