# Authors

## Goals

To have a way to specify the author(s) of a project. This also includes the
concept of maintainers.

The [core metadata](https://packaging.python.org/specifications/core-metadata/)
file format supports 4 related fields (as of version 2.1):

* Author: A string containing the author’s name at a minimum; additional
  contact information may be provided.
* Author-email: A string containing the author’s e-mail address. It can contain
  a name and e-mail address in the legal forms for a RFC-822 `From:` header.
* Maintainer: A string containing the maintainer’s name at a minimum;
  additional contact information may be provided.
* Maintainer-email: A string containing the maintainer’s e-mail address. It can
  contain a name and e-mail address in the legal forms for a RFC-822 `From:`
  header.

Things of note:

* All fields are optional (i.e. a package does not need to specify an author).
* Although all the field names are singluar, there iare no rules saying they
  must contain only one person.
* The author and maintainer fields are free-form. It is common to seperate each
  entry (person) with either a comma or newline (yes, these fields can contain
  multiple lines).
* The email fields can use any form allowed in a typical email header. This
  means that the field can contain multiple entries (separated by comma), and
  each entry can contain the person’s name, e.g.
  `"C. Schultz" <cschultz@example.com>, snoopy@peanuts.com`.


## Comparisons

### Flit and Setuptools
All have the same four fields as the core metadata specification, which are
mapped directly.

### Poetry
Has an [`authors` field](https://poetry.eustace.io/docs/pyproject/#authors) which
is an array of `name <email>` entries. It is not clear how this field is mapped
into core metadata fields.

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

* All formats can accept an arbitrary number of people.
  - Flit and Setuptools use a string-based format to represent multiple people.
  - Poetry, Rust, and npm represent multiple people in a structured format.
* Everyone has either an `author` or `authors` field.
* How people specify metadata on a person varies.
  - Flit and Setuptools have separate fields; the email fields accept
    `name <email>` formatting, while the name fields are free-form.
  - Poetry and Rust accept `name <email>` formatting.
  - npm has structured data.
* Only npm offered more than name and email in a structured way.
  - Flit and Setuptools allow putting extra information directly in the
    author/maintainer string.

## Discussions

The core metadata’s fields are misnamed, which is unfortunate. But we don’t
really need to change that. It is enough for a tool to hide this quirk from
end users, and convert structured data into text behind the scenes:

```toml
# User supplies in pyproject.toml
[package]
name = "peanuts"

[[package.author]]
name = "C. Schultz"
email = "cschultz@example.com"
detail = "Universal Features Syndicate, Los Angeles, CA"

[[package.author]]
name = "Charlie Brown"

[[package.author]]
email = "snoopy@peanuts.com"
```

which can be rendered into:

```
Author: C. Schultz, Universal Features Syndicate, Los Angeles, CA
        Charlie Brown
        snoopy@peanuts.com
Author-email: "C. Schultz" <cschultz@example.com>, snoopy@peanuts.com
```
