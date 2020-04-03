# Dependency Grouping

TODO: Expand the document to include more detailed discussions on each format.

| Format                                                                      | Environmental      | Logical                    |
| --------------------------------------------------------------------------- | ------------------ | -------------------------- |
| [Core metadata](https://packaging.python.org/specifications/core-metadata/) | Inline             | Inline<sup>1</sup>         |
| Pipfile                                                                     | Inline             | Group                      |
| Poetry                                                                      | Inline             | Inline<sup>2</sup>         |
| Flit                                                                        | Inline             | Group<sup>6</sup>          |
| Setuptools                                                                  | Inline<sup>3</sup> | Group<sup>4</sup>          |
| Cargo                                                                       | Group              | Group + Inline<sup>5</sup> |
| package.json                                                                | *Not possible*     | Group                      |

* **Inline**: All dependencies are defined together, with grouping information embedded in each dependency declaration.
* **Group**: Different groups of dependencies are defined in different sections.

<sup>1</sup> A package first defines group labels (`Provides-Extra`), and mark each of its dependencies with group(s) the dependency is included in using the `extra` marker.

<sup>2</sup> `optional = true` marks a dependency as optional. Each optional dependency forms a group named after itself.

<sup>3</sup> Also allows using the group strategy with “nameless” `extras_require` keys, but now [seems to favour](https://github.com/pypa/setuptools/commit/37a48e9a7a5ae5ac770b05b8f1ff52bdceda3cae) the inline format defined in [PEP 508](https://www.python.org/dev/peps/pep-0508/).

<sup>4</sup> It is possible to mark a logical group inline by exploiting PEP 508:

```python
setup(
    ...
    install_requires: ["requirement_name ; extra == 'extra_name'"],
    extras_require: {"extra_name": []},
)
```

but AFAICT this is not proper configuration, just “happens to work.”

<sup>5</sup> Dev dependencies are declared separately in their own group. Other logically grouped dependencies (call *features*) are listed together with required ones (with `optional = true`), and are then grouped by a seperate `features` definition.

<sup>6</sup> Flit has [reserved groups for `test`, `doc`, and `dev`](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section). They are all installed when one [installs the `develop` dependencies](https://flit.readthedocs.io/en/latest/cmdline.html#cmdoption-flit-install-deps).
