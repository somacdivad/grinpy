import sys
sys.path.append('../')

import grinpy as gp
import numpy as np


G = gp.circular_ladder_graph(10)
chromatic_number = gp.chromatic_number(G, method='ilp')
print('Chromatic number (ILP): {}'.format(chromatic_number))
