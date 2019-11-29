# Authors

## Goals
To have a way to specify the author(s) of a project. This also includes the
concept of maintainers.

## Comparisons

### Flit
Has
[`author` and `author-email` fields](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section)
which only support a single author.

It also has `maintainer` and `maintainer-email` fields to support a single
maintainer.

### Setuptools
Has
[`author` and `author_email` fields](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata)
which only support a single author.

It also has `maintainer` and `maintainer_email` fields which support only a single
maintainer.

### Poetry
Has an [`authors` field](https://poetry.eustace.io/docs/pyproject/#authors) which
is an array of `name <email>` entries.

### Cargo
Has an [`authors` field](https://doc.rust-lang.org/cargo/reference/manifest.html#the-authors-field-optional)
which is an array of authors. Email addresses are optional and may be included
via the `name <email>` format.

Acts as the default name to infer the build names.

### npm
Has an [`author` and `contributor` fields](https://docs.npmjs.com/files/package.json#people-fields-author-contributors).
The `author` field is for a single person, `contributor is an array.

Both fields accept an object that must have a `"name"` key and optionally
`"email"` and `"url"` keys.

## Conclusions
* The number of acceptable people varies
  - Flit and Setuptools only accept at most two people
  - Poetry, Rust, and npm can accept an arbitrary number of people
* Everyone has either an `author` or `authors` field
* How people specify metadata on a person varies
  - Flit and Setuptools has separate fields
  - Poetry and Rust accept `name <email>` formatting
  - npm has structured data
* Only npm offered more than name and email
