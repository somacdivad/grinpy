import grinpy as gp
import pytest


class TestDegree:
    def setup_class(self):
        G = gp.Graph()
        G.add_edge(0, 1)
        G.add_edge(0, 2)
        G.add_edge(1, 2)
        G.add_edge(0, 3)
        G.add_edge(3, 4)
        G.add_edge(3, 5)
        self.G = G

    def test_degree_sequence(self):
        D = gp.degree_sequence(self.G)
        assert D == [3, 2, 2, 3, 1, 1]

    def test_max_degree(self):
        maxDegree = gp.max_degree(self.G)
        assert maxDegree == 3

    def test_min_degree(self):
        minDegree = gp.min_degree(self.G)
        assert minDegree == 1

    def test_average_degree(self):
        avgDegree = gp.average_degree(self.G)
        assert avgDegree == 2

    def test_number_of_nodes_of_degree_k(self):
        numNodes = gp.number_of_nodes_of_degree_k(self.G, 2)
        assert numNodes == 2

    def test_number_of_degree_one_nodes(self):
        numNodes = gp.number_of_degree_one_nodes(self.G)
        assert numNodes == 2

    def test_number_of_min_degree_nodes(self):
        numNodes = gp.number_of_min_degree_nodes(self.G)
        assert numNodes == 2

    def test_number_of_max_degree_nodes(self):
        numNodes = gp.number_of_max_degree_nodes(self.G)
        assert numNodes == 2

    def test_complete_graph_is_regular(self):
        G = gp.complete_graph(4)
        assert gp.is_regular(G) == True

    def test_star_is_not_regular(self):
        G = gp.star_graph(2)
        assert gp.is_regular(G) == False

    def test_non_integral_value_raises_TypeError_is_k_regular(self):
        with pytest.raises(TypeError):
            G = gp.trivial_graph()
            gp.is_k_regular(G, 1.5)

    def test_K5_is_4_regular(self):
        G = gp.complete_graph(5)
        assert gp.is_k_regular(G, 4) == True

    def test_star_is_not_2_regular(self):
        G = gp.star_graph(2)
        assert gp.is_k_regular(G, 2) == False

    def test_K4_is_cubic(self):
        G = gp.complete_graph(4)
        assert gp.is_cubic(G) == True

    def test_K4_is_not_cubic(self):
        G = gp.complete_graph(5)
        assert gp.is_cubic(G) == False

    def test_sub_cubic(self):
        assert gp.is_sub_cubic(self.G) == True

    def test_K5_is_not_sub_cubic(self):
        G = gp.complete_graph(5)
        assert gp.is_sub_cubic(G) == False
