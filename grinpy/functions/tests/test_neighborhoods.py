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
        N0 = gp.neighborhood(G, 0)
        N1 = gp.neighborhood(G, 1)
        N2 = gp.neighborhood(G, 2)
        N3 = gp.neighborhood(G, 3)
        N4 = gp.neighborhood(G, 4)
        N5 = gp.neighborhood(G, 5)
        assert(N0 == [1, 2, 3])
        assert(N1 == [0, 2])
        assert(N2 == [0, 1])
        assert(N3 == [0, 4, 5])
        assert(N4 == [3])
        assert(N5 == [3])

    def test_closed_neighborhood(self):
        G = self.G
        N0 = gp.closed_neighborhood(G, 0)
        N1 = gp.closed_neighborhood(G, 1)
        N2 = gp.closed_neighborhood(G, 2)
        N3 = gp.closed_neighborhood(G, 3)
        N4 = gp.closed_neighborhood(G, 4)
        N5 = gp.closed_neighborhood(G, 5)
        assert(N0 == [0, 1, 2, 3])
        assert(N1 == [0, 1, 2])
        assert(N2 == [0, 1, 2])
        assert(N3 == [0, 3, 4, 5])
        assert(N4 == [3, 4])
        assert(N5 == [3, 5])

    def test_are_neighbors(self):
        G = self.G
        t1 = gp.are_neighbors(G, 0, 1)
        t2 = gp.are_neighbors(G, 0, 4)
        t3 = gp.are_neighbors(G, 0, [1, 4])
        t4 = gp.are_neighbors(G, 0, [4, 5])
        assert(t1 == True)
        assert(t2 == False)
        assert(t3 == True)
        assert(t4 == False)