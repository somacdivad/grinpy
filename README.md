[![Build Status](https://travis-ci.org/somacdivad/grinpy.svg?branch=master)](https://travis-ci.org/somacdivad/grinpy) [![BCH compliance](https://bettercodehub.com/edge/badge/somacdivad/grinpy?branch=master)](https://bettercodehub.com/)

# GrinPy
*A NetworkX extension for calculating graph invariants.*

### What is it?
Grinpy is still in development. We are working hard to finish the first build. Our aim is to create an easy-to-use extension for NetworkX for computing all kinds of graph invariants.

### How do I use it?
```python
>>> import grinpy as gp
>>> G = gp.petersen_graph()
>>> gp.independence_number(G)
4
```

Full documentation will be released soon.

### Why does it exist?
The motivation for this project is to filter a database of graphs into an ordered tree of subsets. The graphs in this database a relatively small (no more than 16 - 20 vertices) and in the interest of speed we have written brute
force algorithms for finding many of the NP-hard invariants. After beginning to work on this problem, we decided to go ahead and work on a working of GrinPy. After the first build, we will work on improving our algorithms.
