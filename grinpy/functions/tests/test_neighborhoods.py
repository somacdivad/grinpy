import grinpy as gp

class TestNeighborhoods():
    def setup_class(self):
        G = gp.Graph()
        G.add_edge(0, 1)
        G.add_edge(0, 2)
        G.add_edge(1, 2)
        G.add_edge(0, 3)
        G.add_edge(3, 4)
        G.add_edge(3, 5)
        self.G = G

    def test_neighborhood(self):
        G = self.G
        assert(gp.neighborhood(G, 0) == [1, 2, 3])
        assert(gp.neighborhood(G, 1) == [0, 2])
        assert(gp.neighborhood(G, 2) == [0, 1])
        assert(gp.neighborhood(G, 3) == [0, 4, 5])
        assert(gp.neighborhood(G, 4) == [3])
        assert(gp.neighborhood(G, 5) == [3])

    def test_closed_neighborhood(self):
        G = self.G
        assert(gp.closed_neighborhood(G, 0) == [0, 1, 2, 3])
        assert(gp.closed_neighborhood(G, 1) == [0, 1, 2])
        assert(gp.closed_neighborhood(G, 2) == [0, 1, 2])
        assert(gp.closed_neighborhood(G, 3) == [0, 3, 4, 5])
        assert(gp.closed_neighborhood(G, 4) == [3, 4])
        assert(gp.closed_neighborhood(G, 5) == [3, 5])

    def test_are_neighbors(self):
        G = self.G
        assert(gp.are_neighbors(G, 0, 1) == True)
        assert(gp.are_neighbors(G, 0, 4) == False)
        assert(gp.are_neighbors(G, 0, [1, 4]) == True)
        assert(gp.are_neighbors(G, 0, [4, 5]) == False)
