[![Build Status](https://travis-ci.org/somacdivad/grinpy.svg?branch=master)](https://travis-ci.org/somacdivad/grinpy) [![Build status](https://ci.appveyor.com/api/projects/status/aqqnfhlce26f09xn/branch/master?svg=true)](https://ci.appveyor.com/project/somacdivad/grinpy/branch/master) [![BCH compliance](https://bettercodehub.com/edge/badge/somacdivad/grinpy?branch=master)](https://bettercodehub.com/) [![codecov](https://codecov.io/gh/somacdivad/grinpy/branch/master/graph/badge.svg)](https://codecov.io/gh/somacdivad/grinpy) [![Documentation Status](https://readthedocs.org/projects/grinpy/badge/)](http://grinpy.readthedocs.io/en/latest/)

# GrinPy
*A NetworkX extension for calculating graph invariants.*

### What is it?
GrinPy is an extension for NetworkX used for calculating graph invariants of
simple graphs.

NP-hard invariants in this version include:

* Chromatic number
* Clique number
* Independence number
* Domination number
* Total domination number
* Connected domination number
* Independent domination number
* Power domination number
* Zero forcing number
* Total zero forcing number
* Connected zero forcing number
* Minimum maximal matching number
* Generalized *k* versions of almost all of the above invariants

Other invariants included are:

* Annihilation number
* Matching number
* Residue
* Slater number
* Sub-*k*-domination number

In addition to the graph invariants listed above, we have included some
simple checks for structural properties of a graph:

* `is_triangle_free`
* `is_bull_free`
* `is_claw_free`

### How do I use it?
Full documentation is available at [https://grinpy.rtfd.io](https://grinpy.rtfd.io).

You can install Grinpy from the command line with `pip`:

```
pip install grinpy
```

Here is a sample of how to calculate the independence number:
```python
>>> import grinpy as gp
>>> G = gp.petersen_graph()
>>> gp.independence_number(G)
4
```

GrinPy automatically imports [NetworkX](https://github.com/networkx/networkx) and provides all of the NetworkX classes and methods in the same interface.

### Why does it exist?
The motivation for this project is to filter a database of graphs into an
ordered tree of subsets. This database will be used in an experimental automated
conjecturing program. In creating the required packages for this database, we
realized that a Python package for calculating graph invariants would be
useful for professional research and for graph theory education.

### License
Released under the 3-Clause BSD license (see `LICENSE.txt`):

    Copyright (C) 2017 GrinPy Developers
    David Amos <amosd2@tamu.edu>
    Randy Davila <davilar@uhd.edu>
