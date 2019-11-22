# Include/Exclude Files

There are two types of Python package distributions we care about: sdist and wheel. A wheel tends to only contain stuffs relevant at runtime (besides metadata), but an sdist usually contains more, such as documentation and tests. We will discuss each variant when it’s relevant.

## Comparisons

### Setuptools

Convoluted.

Setuptools makes an distinction between package files and data files. Package files are those importable in Python (but not `*.pyc`; they don’t make sense anyway), and anything else is data.

Packages are supplied to the `packages`, `py_modules`, or `namespace_packages`. Each entry is their import name (not filename). Those entries are combined with `package_dir` to identify them in the project tree. Two utility functions `find_packages()` and `find_namespace_packages()` can be used to automatically discover and list packages recursively, otherwise the user needs to spell out each package (and each subpackage etc.) manually.

Data in each package are supplied with the `package_data` mapping. Or a `include_package_data` key can be set to true to let Setuptools automatically consult `MANIFEST.in` and include all matching files in each package.

A `MANIFEST.in` file is generally needed besides the setup file, in order to correctly include data files. This manifest file also dictates what goes into the sdist, so you can have a file going into both sdist and wheel (by listing it in both places, or use `include_package_data`), or only in sdist but not wheel (by only listing it in `MANIFEST.in`).

### Flit

One (outmost) package per project, specified with the `module` key. The package should be found at the project root, or in a `src` directory (Flit 2.0+). All files in the package are automatically included (including subpackages), and nothing else.

A `[tool.flit.sdist]` can be used to specify what files you want the sdist to exclude/include based on the wheel.

TODO: Does Flit automatically exclude certain files, e.g. `*.pyc`? How about extension modules?

### Poetry

Automatically include a package named the same as the project in the project root, and include all files in it that make sense. Packages are discovered recursively.

Customisation is possible through a `packages` key. You can specify to include more than one package, packages with arbitrary names, or under different prefixes. it is also possible to override the default inclusion rule.

Files not belonging to a package can be specified by a `include` key. Exclusion is done with `exclude`. By default, `exclude` uses VCS ignore rules. Exclude overrides include.

TODO: What is Poety’s default inclusion rule?

### packages.json

All project files are included by default (except [those always ignored](https://docs.npmjs.com/files/package.json#files)). More ignore rules can be added to a file `.npmignore`; `.gitignore` is consulted if `.npmignore` does not exist.

Inclusion rules can be customised, but some files are unconditionally included.

### Cargo

The patterns specified in the `exclude` field identify a set of files that are not included, and the patterns in `include` specify files that are explicitly included. Include overrides exclude.

If git is being used for a package, the `exclude` field will be seeded with the `gitignore` settings from the repository.

TODO: What is the default inclusion rule?
