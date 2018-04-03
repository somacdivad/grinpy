import sys
sys.path.append('../')

import grinpy as gp
import numpy as np


G = gp.circular_ladder_graph(10)
chromatic_number = gp.chromatic_number(G, method='ram-rama')
print('Chromatic number (Ram-Rama): {}'.format(chromatic_number))
