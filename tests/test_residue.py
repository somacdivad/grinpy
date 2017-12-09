from grinpy import grinpy as gp
from math import ceil

class TestResidue():
    def test_residue_of_complete_graph_is_1(self):
        for i in range(1, 11):
            G = gp.complete_graph(i)
            assert(gp.residue(G) == 1)

    def test_residue_of_cycle_is_third_of_order(self):
        for i in range(3, 13):
            G = gp.cycle_graph(i)
            assert(gp.residue(G) == ceil(G.order() / 3))

    def test_2_residue_of_complete_graph_is_three_halves(self):
        for i in range(3, 13):
            G = gp.complete_graph(i)
            assert(gp.k_residue(G, 2) == 1.5)
