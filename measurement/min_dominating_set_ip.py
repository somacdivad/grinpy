import sys
sys.path.append('../')

import grinpy as gp
import numpy as np


# Circular ladder graph of length 10 (20 vertices)
G = gp.circular_ladder_graph(10)
# compute a smallest dominating set and print its length
ds = gp.min_dominating_set_ip(G)
print('Domination number (IP): ' + str(len(ds)))
