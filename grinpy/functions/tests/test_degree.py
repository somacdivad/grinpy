import grinpy as gp

class TestDegree():
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
        assert(gp.degree_sequence(self.G) == [3, 2, 2, 3, 1, 1])

    def test_max_degree(self):
        assert(gp.max_degree(self.G) == 3)

    def test_min_degree(self):
        assert(gp.min_degree(self.G) == 1)

    def test_average_degree(self):
        assert(gp.average_degree(self.G) == 2)

    def test_number_of_nodes_of_degree_k(self):
        assert(gp.number_of_nodes_of_degree_k(self.G, 2) == 2)

    def test_number_of_degree_one_nodes(self):
        assert(gp.number_of_degree_one_nodes(self.G) == 2)

    def test_number_of_min_degree_nodes(self):
        assert(gp.number_of_min_degree_nodes(self.G) == 2)

    def test_number_of_max_degree_nodes(self):
        assert(gp.number_of_max_degree_nodes(self.G) == 2)
