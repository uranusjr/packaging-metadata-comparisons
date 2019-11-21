# Long description

## Goals
Provide a way to include the long description as shown by a package index
(typically a README file). There also needs to be a way to determine/specify the
encoding for proper rendering.

## Comparison

### Flit

Has a
[`description-file` field](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section)
which takes a file path relative to `pyproject.toml`. The file is expected to
have a `.md`, `.txt`, or `.rst` file extension to infer the encoding.

### Setuptools
Supports either a file path or string in its
[`long_description` field](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata).
It also supports an explicit `long_description_content_type` field to specify the
encoding.

### Poetry
Has a [`readme` field](https://poetry.eustace.io/docs/pyproject/#readme) that
takes a file path. File must end in either `.md` or `.rst` to infer the encoding.

### Cargo
Has a
[`readme` field](https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata)
that takes a file path. The documentation does not specify what encodings are
supported, but based on how the Rust community very much supports Markdown the
suspicion is Cargo/crates.io simply assumes Markdown as it's designed to never
fail rendering.

### npm
Has a [`description` field](https://docs.npmjs.com/files/package.json#description-1).
There is no specification of the encoding.

Npm does
[automatically include a file named `README`](https://docs.npmjs.com/files/package.json#files)
with any file extension. The
[README file is what npm will render](https://docs.npmjs.com/about-package-readme-files)
as the long description at npmjs.com. The documentation explicitly suggests
using Markdown and naming the file `README.md`, suggesting the file extension is
how one denotes whether the file is Markdown or not.

## Conclusions
* All of the tools support using a file (some implicitly, some with an explicit path)
* All of the tools support Markdown
* All the Python tools support Markdown or reStructuredText
