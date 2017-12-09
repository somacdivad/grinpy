# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""Functions for computing various structural properites."""

import networkx as nx
import itertools

def is_triangle_free(G):
    """Returns a boolean value according to G containing an induced triangle.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    is_triangle_free : boolean
                       True if G containes no induced triangle. False if G contains at least one induced triangle.

    Examples
    --------
    >>> G = nx.Graph([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]) # The complete graph K_4
    >>> nx.is_triangle_free(G)
    False
    """
    # define a triangle graph, also known as the complete graph K_3
    triangle = nx.Graph([(0,1),(1,2),(2,0)])
    
    # assume first that G is triangle-free
    triangle_free = True
    
    # enumerate over all possible combinations of 3 vertices contained in G
    for s in set(itertools.combinations(G.nodes(), 3)):
          H = G.subgraph(list(s))
          if nx.is_isomorphic(H,triangle):
              return False
    return triange_free
  
    
   

def is_bull_free(G):
    """Returns a boolean value according to G containing an induced triangle.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    is_bull_free : boolean
                       True if G containes no induced bull. False if G contains at least one induced bull.
                       Recall that a bull is a triangle with two pendants added to two vertices of the triangle.

    Examples
    --------
    >>> G = nx.Graph([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]) # The complete graph K_4
    >>> nx.is_bull_free(G)
    True
    """
    # define a bull graph, also known as the graph obtained from the complete graph K_3 by addiing two pendants
    bull = nx.Graph([(0,1), (0,2),(1,2),(1,3), (2,4)])
    
    # assume first that G is bull-free
    bull_free = True
    
    # enumerate over all possible combinations of 5 vertices contained in G
    for s in set(itertools.combinations(G.nodes(), 5)):
          H = G.subgraph(list(s))
          if nx.is_isomorphic(H,bull):
              return False
    return bull_free
  
  
  
def is_claw_free(G):
    """Returns a boolean value according to G containing an induced claw.

    Parameters
    ----------
    G : graph
        A NetworkX graph.

    Returns
    -------
    is_claw_free : boolean
                       True if G containes no induced claw. False if G contains at least one induced claw.
                       Recall that a claw is the complete bipartite graph K_1,3

    Examples
    --------
    >>> G = nx.Graph([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]) # The complete graph K_4
    >>> nx.is_bull_free(G)
    True
    """
    # define a claw graph, also known as the complete bipartite graph K_1,3
    claw = nx.Graph([(0,1), (0,2), (0,3)])
    
    # assume first that G is claw-free
    claw_free = True
    
    # enumerate over all possible combinations of 4 vertices contained in G
    for s in set(itertools.combinations(G.nodes(), 4)):
          H = G.subgraph(list(s))
          if nx.is_isomorphic(H,claw):
              return False
    return claw_free
