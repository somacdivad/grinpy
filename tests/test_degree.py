from grinpy import grinpy as gp

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
        D = gp.degree_sequence(self.G)
        assert(D == [3, 2, 2, 3, 1, 1])

    def test_max_degree(self):
        maxDegree = gp.max_degree(self.G)
        assert(maxDegree == 3)

    def test_min_degree(self):
        minDegree = gp.min_degree(self.G)
        assert(minDegree == 1)

    def test_average_degree(self):
        avgDegree = gp.average_degree(self.G)
        assert(avgDegree == 2)

    def test_number_of_nodes_of_degree_k(self):
        numNodes = gp.number_of_nodes_of_degree_k(self.G, 2)
        assert(numNodes == 2)

    def test_number_of_degree_one_nodes(self):
        numNodes = gp.number_of_degree_one_nodes(self.G)
        assert(numNodes == 2)

    def test_number_of_min_degree_nodes(self):
        numNodes = gp.number_of_min_degree_nodes(self.G)
        assert(numNodes == 2)

    def test_number_of_max_degree_nodes(self):
        numNodes = gp.number_of_max_degree_nodes(self.G)
        assert(numNodes == 2)
