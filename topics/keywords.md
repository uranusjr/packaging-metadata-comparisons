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

## Data points
* There are 203,414 projects on PyPI with 225,623 keywords in total, making the mean 1.1091812756250798 keywords/project
* The median count is 0
* https://pypi.org/project/PyGeodesy/ has the largest number of keywords on PyPI at 111
* More than ...
  - 0 keywords: 77,591
  - 5 keywords: 9,434
  - 8 keywords: 2,380
  - 9 keywords: 1,555 (< 1%)
  - 10 keywords: 1,095
  - 16 keywords: 204
  - 17 keywords: 156 (< 0.1%)
  - 32 keywords: 21
  - 33 keywords: 19 (< 0.01%)
  - 101 keywords: 1
