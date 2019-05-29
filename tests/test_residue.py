import grinpy as gp
from math import ceil


class TestResidue:
    def test_residue_of_complete_graph_is_1(self):
        for i in range(1, 11):
            G = gp.complete_graph(i)
            assert gp.residue(G) == 1

    def test_residue_of_cycle_is_third_of_order(self):
        for i in range(3, 13):
            G = gp.cycle_graph(i)
            assert gp.residue(G) == ceil(G.order() / 3)

    def test_2_residue_of_complete_graph_is_three_halves(self):
        for i in range(3, 13):
            G = gp.complete_graph(i)
            assert gp.k_residue(G, 2) == 1.5

    def test_k_residual_index_of_peterson_graph_is_2(self):
        G = gp.petersen_graph()
        assert gp.k_residual_index(G) == 2

    def test_k_residual_index_of_trivial_graph_is_1(self):
        G = gp.trivial_graph()
        assert gp.k_residual_index(G) == 1
