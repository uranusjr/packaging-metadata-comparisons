# Keywords

## Goals
To have a way to specify keywords about the project.

## Comparisons

Tool | Field | Format | Length
--- | --- | --- | ---
Flit | [`keywords`](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section) | comma-separated | ♾
Setuptools | [`keywords`](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata) | comma-separated | ♾
Poetry | [`keywords`](https://poetry.eustace.io/docs/pyproject/#keywords) | array | <=5
Cargo | [`keywords`](https://doc.rust-lang.org/cargo/reference/manifest.html#package-metadata) | array | <=5
npm | [`keywords`](https://docs.npmjs.com/files/package.json#keywords) | array | ♾


## Conclusions
* All tools have a `keywords` field
* All tools accept _at least_ 5 keywords
* Format is either comma-separated string or array of strings
