# Declaring Dependency Entries

## Goals

Declaration formats are compared to the [PEP 508](https://www.python.org/dev/peps/pep-0508/) specification, to check whether each one of them is able to express all possible scenarios of depending on a Python package.

Judgements are also made to formats on whether they are able to ultilise the TOML syntax to provide better readability, prevent user from typos, and help user discover possibilities.

## Non-goals

### How dependencies are grouped into sections

We only compare how formats declare *each* dependency. How dependencies are grouped into sections (*a la* `extras_require`) is compared in its own document. 

### What tools do with the declarations

The document does not go into how the tools actually uses the declared dependencies. For example, packaging tools may convert them into `Requires-Dist`entries in package metadata, or “lock” them into pinned distribution declarations.

## Comparisons

### String-based formats

[Flit](https://flit.readthedocs.io/en/latest/pyproject_toml.html) uses the PEP 508 format straight-up in `pyproject.toml`, as do Setuptools in `setup.py` and `setup.cfg`.

#### Advantages

No need to specify anything, it just works. The content can be converted directly into Python package metadata without any transformation, costing minimal effort for packaging tools.

#### Disadvantages

Syntax is arguably more difficult to learn for newcomers.

TOML does not have a way to declare a list of strings using the `[[double-bracket]]`syntax, so you need to put the list inside a section, which can become difficult to read if a project has (say) 10+ dependencies. Take Flit for example:

```toml
[tool.flit.metadata]
requires = [
    "requests >=2.6",
    "configparser; python_version == '2.7'",
]
```

Since each entry is simply a string, this also makes it much more difficult to report early syntax errors with editing tools like syntax highlighting and linters.

### [Pipfile](https://github.com/pypa/pipfile)

```toml
requests = { extras = ['socks'] }
records = '>0.5.0'
pywinusb = { version = "*", os_name = "=='nt'" }
unittest2 = {
    version = ">=1.0,<3.0",
    markers = "python_version >= '3.0' and python_version < '3.4'",
}
```

Pipfile uses a TOML key-value pair to represent a dependency. The key specifying the name, and the value everything else. If value is a string, is a [PEP 440](https://www.python.org/dev/peps/pep-0440/) version specifier (or a literal `*` representing an empty specifier, “any version”).

If value is an object, it may contain the following entries (all optional):

* `version`: A string, interpreted the same as a string value.

* `extras`: A list of strings representing extras the dependency requests.

* `markers`: A string representing the dependency’s environment markers.
  
     * All possible markers except `extra` are available as keys as well, with string values. They are joined with AND on evaluation.

* `file`: A string, specifying this dependency as a URL-based lookup. This conflicts with `version`.

There are other keys allowed for specifying a VCS dependency, and specifying a particular source to resolve a name-based lookup. These are out of scope of PEP 508, and thus not discussed here.

#### Advantages

Utilises the TOML syntax to help the user catch early syntax errors.

The key-value form allows the entries to be declared in a top-level `[section]`, improving readability.

#### Disadvantages

It is not possible to declare the equivalent of the following:

```
django>=2.0; os_name != 'nt'
django>=2.1; os_name == 'nt'
```

Maybe I’m biased since I was responsible to maintain the parser for Pipenv, but it is quite tedious to parse. Maybe it’d be better if we get rid of the top-level marker keys?

Using keys to express context (e.g. `version` and `file`) also means that it is easier to write definitions that are perfectly syntax-wise but make no sematic sense. This makes validation more difficult.

This is probably just personal taste, but I really dislike the `*` specifier.  I would’ve be much happier if it chose to use an empty string instead.

### [Poetry](https://poetry.eustace.io/docs/versions/)

```toml
requests = "^2.13.0"
pathlib2 = { version = "^2.2", python = ["~2.7", "^3.2"] }
foo = [
    { version = "<=1.9", python = "^2.7" },
    { version = "^2.0", python = "^3.4" },
]
```

Poetry uses a TOML key-value pair to represent a dependency. The key specifying the name, and the value everything else. If value is a string, it is a version specifier. The format is similar, but different from PEP 440 (e.g. `~` instead of `~=`, and a  `^` operator). They can all be translated into PEP 440 specifiers.

If value is an object, it can contain the following keys:

* `version`: A string, the version specifier. (Can this be a list of strings?)

* `python`: A string of a list of strings, specifying Python versions this dependency is only requested on.

There are other keys allowed for specifying a VCS or local dependency, a particular source to resolve a name-based lookup, or marking a dependency as optional for sectioning. These are out of scope of PEP 508, and thus not discussed here.

If value is a list, it should contain multiple objects, each using the same format as the object variant. Each object entry represents a dependency request.

#### Advantages

All advantages of Pipfile apply.

It is also possible to express the same-package-different-marker problem with the list-of-object format.

#### Disadvantages

It is only possible to mark a dependency conditional to Python versions (which translates to `python_version`markers) not anything else.

Not possible to provide a URL-based lookup.

Not possible to specify extras.

The documentation is a bit lacking compared to most other formats mentioned in this document.

This is probably just personal taste, but I really dislike the `*` specifier. I would’ve be much happier if it chose to use an empty string instead.




