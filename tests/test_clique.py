import grinpy as gp


class TestIndependence:
    def test_clique_number_of_complete_graph_is_order(self):
        for i in range(1, 11):
            G = gp.complete_graph(i)
            assert gp.clique_number(G) == G.order()
