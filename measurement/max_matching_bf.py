import sys
sys.path.append('../')

import grinpy as gp
import numpy as np


G = gp.circular_ladder_graph(10)
m = gp.max_matching(G)
print('Matching number (brute force): {}'.format(len(m)))
