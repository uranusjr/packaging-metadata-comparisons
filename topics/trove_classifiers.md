# [Trove classifiers](https://pypi.org/classifiers/)

## Goals
To have a way to specify arbitrary trove classifiers.

## Comparisons
Note that other languages do not use trove classifiers and thus will not be
compared against.

### Flit
Has a
[`classifiers` field](https://flit.readthedocs.io/en/latest/pyproject_toml.html#metadata-section)
which takes a list of trove classifiers.

### Setuptools
Has a
[`classifiers` field](https://setuptools.readthedocs.io/en/latest/setuptools.html#metadata)
which accepts a comma-separated list or a file path.

### Poetry
Has a [`classifiers` field](https://poetry.eustace.io/docs/pyproject/#classifiers)
that takes a list of strings. It will also automatically set classifiers based
on the Python requirement and the specified license.

## Conclusions
* All tools accept an arbitrary list of trove classifiers
* All tools named the field `classifiers`
* No one requires any classifiers be specified
