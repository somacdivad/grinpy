# How to build the docs

GrinPy uses Sphinx for generating the API documentation. Pre-built docs can
be found at [https://grinpy.rtfd.io](https://grinpy.rtfd.io).

## Instructions
Install the Python packages required to build the documentation:

```
pip install -r requirements.txt
```

in the `docs/` directory.

Then enter

```
make html
```

to build the HTML documentation. The HTML files can be found in the
`_build/html` subdirectory.
