..  -*- coding: utf-8 -*-

Tutorial
========

.. currentmodule:: grinpy

This guide can help you start working with GrinPy. We assume basic knowledge
of NetworkX. For more information on how to use NetworkX, see the `NetworkX
Documentation <https://https://networkx.github.io/documentation/stable/>`_.

Calculating the Independence Number
-----------------------------------

For this example we will create a cycle of order 5.

.. nbplot::

  >>> import grinpy as gp
  >>> G = gp.cycle_graph(5)

In order to compute the independence number of the cycle, we simply call the `independence_number` method on the graph:

.. nbplot::

  >>> gp.independence_number(G)
  2

It's that simple!

.. note:: In this release (version |version|), all methods are defined only for simple graphs. In future releases, we will expand to digraphs and multigraphs.

Get a Maximum Independent Set
-----------------------------

If we are interested in finding a maximum independent set in the graph:

.. nbplot::

  >>> gp.max_independent_set(G)
  [0, 2]

Determine if a Given Set is Independent
---------------------------------------

We may check whether or not a given set is independent:

.. nbplot::

  >>> gp.is_independent_set(G, [0, 1])
  False
  >>> gp.is_independent_set(G, [1, 3])
  True

General Notes
-------------

The vast majority of NP-hard invariants will include three methods
corresponding to the above examples. That is, for each invariant, there will
be three methods:

-  Calculate the invariant
-  Get a set of nodes realizing the invariant
-  Determine whether or not a given set of nodes meets some necessary
   condition for the invariant.
