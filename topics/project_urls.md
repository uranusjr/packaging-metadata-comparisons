# Project URLs

Package indices often let you specify project-specific URLs such as where to
find documentation, file bugs, etc.

For PyPI there are no required or suggested URLs, although there is special
[support for certain URL names that lead to specific icons](https://github.com/pypa/warehouse/blob/master/warehouse/templates/packaging/detail.html).

## Goals

Provide a way to specify multiple URLs for a project.

## Non-goals

Restrict/suggest URLs that every project should provide (as that involves a
conversation with Warehouse).

## Comparisons

### Flit

There are two places to specify URLs in Flit. a single, generic URL can be
provided in
[`tool.flit.metadata`](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section)
via the `home-page` key.

The other way is in a
[`tool.flit.metadata.urls` section](https://flit.readthedocs.io/en/latest/pyproject_toml.html#urls-subsection)
where each key specifies the name for a URL and the value is the URL itself.

### Setuptools

Like Flit, Setuptools supports both a generic `url` field as well as a
`project_urls` dict which is an aribrary mapping of URL names to URLs in its
[metadata](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata).

### Poetry

Support exists for restricted set of URLs:

- [`homepage`](https://poetry.eustace.io/docs/pyproject/#homepage)  (mapped to Home-page)
- [`repository`](https://poetry.eustace.io/docs/pyproject/#repository) (mapped to Repository of Project-URL)
- [`documentation`](https://poetry.eustace.io/docs/pyproject/#documentation) (mapped to Documentation of Project-URL)

Beta version of Poetry support custom urls in metadata (since [1.0.0a4](https://github.com/sdispater/poetry/releases/tag/1.0.0a4) version) that placed [under tool.poetry.urls section](https://github.com/sdispater/poetry/pull/1137). 

Note: If under this section will be used the same keyword (case sensitive) values defined under tool.poetry section will be overridden.

### Cargo

Must like Poetry, Cargo provides a restricted set of URLs:

- [`documentation`](https://doc.rust-lang.org/cargo/reference/manifest.html#the-documentation-field-optional)
- [`homepage`](https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata)
- [`repository`](https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata)

One interesting difference is because documentation is hosted at https://docs.rs/
and not on https://crates.io/, if the `documentation` link is left out it is
automatically assumed by crates.io to point to the appropriate https://docs.rs/
URL.

Another extra that one can specify in their `cargo.toml` file is links to
badges of various continuous integration systems:

- appveyor
- Circle
- cirrus
- gitlab
- Azure DevOps
- Travis
- codecov
- coveralls

One drawback to this, though, is that the supported CI systems will never be
complete (e.g. [GitHub Actions](https://github.com/features/actions) went public
the week prior to when this was written and it is not supported yet).

### npm
There is support for a restricted set of URLs for a project:
- [`homepage`](https://docs.npmjs.com/files/package.json#homepage)
- [`bugs`](https://docs.npmjs.com/files/package.json#bugs)
- [`repository`](https://docs.npmjs.com/files/package.json#repository)

An interesting thing about `bugs` is you can also specify an email address for
bug reporting.

As for `repository`, there is an extra bit of metadata specifying what kind of
version control the repository uses.

## Conclusions
* All tools support:
  1. Home page
  2. Repository
* Everyone but npm supports:
  1. Home page
  2. Repository
  3. Documentation
* No one required any URLs to be specified
