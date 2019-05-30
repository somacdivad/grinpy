.. GrinPy documentation master file, created by
   sphinx-quickstart on Sun Dec  3 20:56:57 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GrinPy
=================

GrinPy is a NetworkX extension for calculating graph invariants. This extension
imports all of NetworkX into the same interface as GrinPy for easy of use and
provides the following extensions:

-  extended functional interface for graph properties
-  calculation of NP-hard invariants such as: independence number, domination
   number and zero forcing number
-  calculation of several invariants that are known to be related to the
   NP-hard invariants, such as the residue, the annihilation number and the
   sub-domination number

Our goal is to provide the most comprehensive list of invariants. We will be
continuing to add to this list as time goes on, and we invite others to join
us by contributing their own implementations of algorithms for computing new
or existing GrinPy invariants.

Audience
--------
We envision GrinPy's primary audience to be professional mathematicians and
students of mathematics. Computer scientists, electrical engineers, physicists,
biologists, chemists and social scientists may also find GrinPy's extensions
to the standard NetworkX package useful.

History
-------
Grinpy was originally created to aid the developers, David Amos and
Randy Davila, in creating an ordered tree of graph databases for use in an
experimental automated conjecturing program. It quickly became clear that
a Python package for calculating graph invariants would be useful. GrinPy was
created in November 2017 and is still in its infancy. We look forward to what
the future brings!

Free Software
-------------
GrinPy is free software; you can redistribute it and/or modify it under the
terms of the :doc:`3-clause BSD license </license>`, the same license that
NetworkX is released under. We greatly appreciate contributions. Please join us
on `Github <https://github.com/somacdivad/grinpy>`_.

Documentation
-------------

.. only:: html

   :Release: |version|
   :Date: |today|

.. toctree::
   :maxdepth: 2

   tutorial
   reference/index
   license



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
