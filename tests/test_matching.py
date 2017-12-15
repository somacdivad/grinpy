from grinpy import grinpy as gp
import math

class TestMatching():
    def test_matching_number_of_empty_graph_is_0(self):
        for i in range(1, 11):
            G = gp.empty_graph(i)
            assert(gp.matching_number(G) == 0)

    def test_matching_number_of_path_is_ceil_of_half_of_edges(self):
        for i in range(2, 12):
            P = gp.path_graph(i)
            m = math.ceil(gp.number_of_edges(P) / 2)
            assert(gp.matching_number(P) == m)

    def test_matching_number_of_star_is_1(self):
        for i in range(1, 11):
            G = gp.star_graph(i)
            assert(gp.matching_number(G) == 1)

    def test_min_maximal_matching_number_of_star_is_1(self):
        for i in range(1, 11):
            G = gp.star_graph(i)
            assert(gp.min_maximal_matching_number(G) == 1)

    def test_min_maximal_matching_of_P2_through_P4_is_1(self):
        for i in range(2, 5):
            P = gp.path_graph(i)
            assert(gp.min_maximal_matching_number(P) == 1)
