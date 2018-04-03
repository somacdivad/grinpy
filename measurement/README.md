# Profiling GrinPy

The scripts in this directory are intended to be used for profiling GrinPy on
your machine. We recommend using Python's built-in `cProfile` module.

Each script generates the circular ladder graph of length 10 (which has 20
nodes) and executes a single method from GrinPy used for calculating
invariants. The filename for each script matches the method to be profiled.
You may profile with different graphs by altering the code if
necessary.

## Instructions
 To execute, run the following from the command line:

```console
$ python -m cProfile filename.py
```

## Explanation

Files with the `_bf` postfix are methods that compute via *brute force*; that
is, an optimal set is found by searching through all subsets of nodes starting
from singletons (if the invariant is a minimum) or from the full set of nodes
(if the invariant is a maximum). In some cases, the search is sped up by
optimizing according to some simple upper or lower bound with a
polynomial time algorithm.

Files with the `_ip` postfix are methods that compute via *integer programming*.
GrinPy uses [PuLP](https://github.com/coin-or/pulp "PuLP LP modeler") to solve the
integer programs.
