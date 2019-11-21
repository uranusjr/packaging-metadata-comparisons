# Packaging Metadata Comparions

Get an idea how various packaging systems declare metadata, in an effort to figure out how pyproject.toml should do it.

## Topics

<!-- To contributors: Do not put anything between topic_gen_start and topic_gen_finish; those are auto-generated by `script/topics_gen.py`. -->

<!-- topics_gen_start -->
* [Dependency Entries](topics/dependency-entries.md)
* [Dependency Grouping](topics/dependency-grouping.md)
* [License](topics/license.md)
* [Long description](topics/long_description.md)
* [Project URLs](topics/project_urls.md)
* [Version](topics/version.md)
* [[Trove classifiers](https://pypi.org/classifiers/)](topics/trove_classifiers.md)
<!-- topics_gen_finish -->

## Please help out!

Find any mistakes or misunderstandings? Don’t agree with some observations? Think I should discuss a tool but haven’t? Have insights on a metadata field not yet mentioned?

Please file a pull request!

Some projects that are being looked at for comparison:

- Python
     - [Flit](https://flit.readthedocs.io/)
     - [Setuptools](https://setuptools.readthedocs.io)
     - [Pipenv](https://pipenv.kennethreitz.org)
     - [Poetry](https://poetry.eustace.io/)
- Other languages
     - [Cargo](https://doc.rust-lang.org/cargo/guide/) ([`Cargo.toml` spec](https://doc.rust-lang.org/cargo/reference/manifest.html))
     - [npm](https://docs.npmjs.com/) ([`package.json` spec](https://docs.npmjs.com/files/package.json))
