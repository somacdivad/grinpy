# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing independence related invariants for a graph."""

# imports
from itertools import combinations
from grinpy import neighborhood, nodes, number_of_nodes, set_neighborhood
from grinpy.invariants.dsi import annihilation_number
from pulp import LpBinary, LpMaximize, LpProblem, LpVariable, lpSum

__all__ = ['is_independent_set',
           'is_k_independent_set',
           'max_k_independent_set',
           'max_independent_set_bf',
           'max_independent_set_ip',
           'independence_number',
           'k_independence_number'
           ]


# methods
def is_independent_set(G, nodes):
    """Return whether or not the *nodes* comprises an independent set.

    An set *S* of nodes in *G* is called an *independent set* if no two nodes
    in S are neighbors of one another.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    Returns
    -------
    bool
        True if the the nodes in *nodes* comprise an independent set, False
        otherwise.

    See Also
    --------
    is_k_independent_set
    """
    S = set(n for n in nodes if n in G)
    return set(set_neighborhood(G, S)).intersection(S) == set()


def is_k_independent_set(G, nodes, k):
    """Return whether or not the nodes in *nodes* comprise an a k-independent
    set.

    A set *S* of nodes in *G* is called a *k-independent set* it every node
    in S has at most *k*-1 neighbors in S. Notice that a 1-independent set
    is equivalent to an independent set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    nodes : list, set
        An iterable container of nodes in G.

    k : int
        A positive integer.

    Returns
    -------
    bool
        True if the nodes in *nodes* comprise a k-independent set, False
        otherwise.

    See Also
    --------
    is_independent_set
    """
    if k == 1:
        return is_independent_set(G, nodes)
    else:
        S = set(n for n in nodes if n in G)
        for v in S:
            N = set(neighborhood(G, v))
            if len(N.intersection(S)) >= k:
                return False
        return True


def max_k_independent_set(G, k):
    """Return a largest k-independent set of nodes in *G*.

    The method used is brute force, except when *k*=1. In this case, the search
    starts with subsets of *G* with cardinality equal to the annihilation
    number of *G*, which was shown by Pepper to be an upper bound for the
    independence number of a graph, and then continues checking smaller subsets
    until a maximum independent set is found.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    list
        A list of nodes comprising a largest k-independent set in *G*.

    See Also
    --------
    max_independent_set
    """
    # set the maximum for the loop range
    rangeMax = number_of_nodes(G) + 1
    if k == 1:
        rangeMax = annihilation_number(G) + 1
    # loop through subsets of nodes of G in decreasing order of size until a
    # k-independent set is found
    for i in reversed(range(rangeMax)):
        for S in combinations(nodes(G), i):
            if is_k_independent_set(G, S, k):
                return list(S)


def max_independent_set_bf(G):
    """Return a largest independent set of nodes in *G*.

    The method used is a modified brute force search. The search
    starts with subsets of *G* with cardinality equal to the annihilation
    number of *G*, which was shown by Pepper to be an upper bound for the
    independence number of a graph, and then continues checking smaller subsets
    until a maximum independent set is found.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes comprising a largest independent set in *G*.

    See Also
    --------
    max_k_independent_set
    """
    return max_k_independent_set(G, 1)


def max_independent_set_ip(G):
    """Return a largest independent set of nodes in *G*.

    This method uses integer programming to solve for a largest independent
    set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    list
        A list of nodes comprising a largest independent set in *G*.

    See Also
    --------
    max_k_independent_set
    """
    # Initialize the problem
    prob = LpProblem('independence_number', LpMaximize)
    variables = []

    # Pairs is a list which keeps track of the indicies of the variables
    pairs = list()

    # Set the variables
    for i in range(G.order()):
        x = LpVariable('x{}'.format(i+1), 0, 1, LpBinary)
        pairs.append((i, x))
        variables.append(x)

    # Set the independence number objective function
    prob += lpSum(variables)

    # Set the integer program contraints
    for e in G.edges():
        prob += pairs[int(e[0])][1] + pairs[int(e[1])][1] <= 1

    # Solve the IP
    prob.solve()

    # Now that the IP has been solved, the variables have been assigned
    # values which acheive the optimal (might not be unique)
    solution_set = []
    for i in range(len(variables)):
        if variables[i].value() == 1:
            solution_set.append(variables[i])

    # Return an optimal independent set
    return list(solution_set)


def independence_number(G):
    """Returns the independence number of G.

    The *independence number* of a graph is the cardinality of a largest
    independent set of nodes in the graph.

    This method uses the `max_independent_set_ip` method to solve for a
    largest independent set and returns the size of this set.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    Returns
    -------
    int
        The independence number of *G*.

    See Also
    --------
    k_independence_number
    """
    return len(max_independent_set_ip(G))


def k_independence_number(G, k):
    """Return a the k-independence number of G.

    The *k-independence number* of a graph is the cardinality of a largest
    k-independent set of nodes in the graph.

    Parameters
    ----------
    G : NetworkX graph
        An undirected graph.

    k : int
        A positive integer.

    Returns
    -------
    int
        The k-independence number of *G*.

    See Also
    --------
    independence_number
    """
    return len(max_k_independent_set(G, k))
