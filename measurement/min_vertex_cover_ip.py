import sys
sys.path.append('../')

import grinpy as gp


G = gp.circular_ladder_graph(10)
vc = gp.min_vertex_cover_ip(G)
print('Vertex Cover Number (ILP): {}'.format(len(vc)))
