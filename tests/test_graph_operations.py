import grinpy as gp


class TestGraphOperations:
    def test_contracting_two_nodes(self):
        G = gp.complete_graph(3)
        gp.contract_nodes(G, [0, 1])
        assert G.has_node(0) == True
        assert G.has_node(2) == True
        assert G.has_node(1) == False
        assert G.has_edge(0, 2) == True
        assert G.has_edge(0, 1) == False
        assert G.has_edge(1, 2) == False

    def test_contracting_single_node_does_not_change_graph(self):
        G = gp.complete_graph(3)
        gp.contract_nodes(G, 0)
        assert G.has_node(0) == True
        assert G.has_node(2) == True
        assert G.has_node(1) == True
        assert G.has_edge(0, 2) == True
        assert G.has_edge(0, 1) == True
        assert G.has_edge(1, 2) == True
