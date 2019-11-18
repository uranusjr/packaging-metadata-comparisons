# License

## Goals
Easily support projects using standard licenses to declare as such through metadata. Also support the specification of the
license text for tools that need to generate third-party notice files.

## Comparisons

Tool | License type | License file
--- | --- | ---
Flit | trove | N
Setuptools | trove | Y
Poetry | SPDX | N
Cargo | SPDX | Y
npm | SPDX | N


### [Flit](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section)
Preference is for specifying the license via [trove classifiers](https://pypi.org/classifiers/). Support is also allowed
through a free-form `license` field which is meant for when a trove classifier doesn't already exist for a license.

There is no support for providing the full license text.

### [Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata)
Setuptools support specifying the appropriate trove classifier. It also supports a free-form `license` field and a
`license_file` field.

### [Poetry](https://poetry.eustace.io/docs/pyproject/#license)
Has users specify a license via their [SPDX license identifier](https://spdx.org/licenses/). The tool then [automatically sets
the trove classifier](https://poetry.eustace.io/docs/pyproject/#classifiers).

There appears to be no way to specify the full text of the license.

### [Cargo](https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata)
Supports [SPDX 2.1 license expressions](https://spdx.org/specifications) in its `license` field. The tool also supports a
`license-file` field.

### [npm](https://docs.npmjs.com/files/package.json#license)
Supports SPDX 2.1 license expressions. Users are encouraged to use the phrase `"SEE LICENSE IN <filename>"` when the license
is non-standard, but there is no explicit support for full license text from a file.
