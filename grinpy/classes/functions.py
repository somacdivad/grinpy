# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functional interface for class methods."""

import grinpy as gp
from grinpy.functions.degree import degree_sequence

__all__ = ["is_graphic", "havel_hakimi_process", "elimination_sequence"]


def is_graphic(sequence):
    """Return whether or not the input sequence is graphic.

    A sequence of positive integers is said to be a *graphic sequence* if there
    exist a graph whose degree sequence is equal to the input sequence, up to
    ordering.

    Parameters
    ----------
    sequence : list, iterable
        A list or other iterable container of integers.

    Returns
    -------
    bool
        True if the input sequence is graphic. False otherwise.
    """
    hh = gp.HavelHakimi(sequence)
    return hh.is_graphic()


def havel_hakimi_process(G):
    """Return an instance of the HavelHakimi class initialized with the degree
    sequence of the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    object
        An instance of the HavelHakimi class initialized with the degree
        sequence of the graph.

    See Also
    --------
    HavelHakimi
    """
    return gp.HavelHakimi(degree_sequence(G))


def elimination_sequence(G):
    """Return the elimination sequence of the graph.

    The *elimination sequence* of a graph is the elimination sequence generated
    by the Havel Hakimi process performed on the degree sequence of the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        The elimination sequence of the graph.
    """
    return havel_hakimi_process(G).get_elimination_sequence()
