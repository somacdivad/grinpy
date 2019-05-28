import grinpy as gp


class TestDegree:
    def test_K5_is_complete_graph(self):
        G = gp.complete_graph(5)
        assert gp.is_complete_graph(G) == True

    def test_C5_is_not_complete_graph(self):
        G = gp.cycle_graph(5)
        assert gp.is_complete_graph(G) == False

    def test_K4_is_not_triangle_free(self):
        G = gp.complete_graph(4)
        assert gp.is_triangle_free(G) == False

    def test_C4_is_triangle_free(self):
        G = gp.cycle_graph(4)
        assert gp.is_triangle_free(G) == True

    def test_K4_is_bull_free(self):
        G = gp.complete_graph(4)
        assert gp.is_bull_free(G) == True

    def test_bull_is_not_bull_free(self):
        G = gp.complete_graph(3)
        G.add_edge(1, 3)
        G.add_edge(2, 4)
        assert gp.is_bull_free(G) == False

    def test_K4_is_claw_free(self):
        G = gp.complete_graph(4)
        assert gp.is_claw_free(G) == True

    def test_S4_is_not_claw_free(self):
        G = gp.star_graph(4)
        assert gp.is_claw_free(G) == False
