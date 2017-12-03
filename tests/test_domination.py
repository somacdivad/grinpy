from grinpy import grinpy as gp

class TestDomination():
    def test_max_degree_vertex_is_dominating_set_of_star(self):
        for i in range(1, 9):
            G = gp.star_graph(i)
            assert(gp.is_k_dominating_set(G, 0, 1) == True)

    def test_min_degree_vertex_is_not_dominating_set_of_star(self):
        for i in range(2, 9):
            G = gp.star_graph(i)
            assert(gp.is_k_dominating_set(G, 1, 1) == False)

    def test_dominating_set_with_nodes_not_in_graph(self):
        G = gp.star_graph(3)
        assert(gp.is_k_dominating_set(G, 4, 1) == False)
        assert(gp.is_k_dominating_set(G, [0, 4], 1) == True)

    def test_max_degree_vertex_is_not_2_dominating_set_of_star(self):
        for i in range(1, 9):
            G = gp.star_graph(i)
            assert(gp.is_k_dominating_set(G, 0, 2) == False)

    def test_min_degree_vertices_are_2_dominating_set_of_star(self):
        for i in range(2, 9):
            G = gp.star_graph(i)
            nodes = [i for i in range(1,i+2)]
            assert(gp.is_k_dominating_set(G, nodes, 2) == True)

    def test_2_dominating_set_with_nodes_not_in_graph(self):
        G = gp.star_graph(3)
        nodes = [1, 2, 3, 4]
        assert(gp.is_k_dominating_set(G, 4, 1) == False)
        assert(gp.is_k_dominating_set(G, nodes, 1) == True)

    def test_no_single_nodes_is_total_dominating_set_of_star(self):
        G = gp.star_graph(3)
        for v in gp.nodes(G):
            assert(gp.is_total_dominating_set(G, v) == False)

    def test_adjacent_vertices_are_total_dominating_set_of_star(self):
        G = gp.star_graph(3)
        for v in gp.nodes(G):
            for u in gp.nodes(G):
                if gp.are_neighbors(G, u, v):
                    assert(gp.is_total_dominating_set(G, [u, v]) == True)

    def test_non_adjacent_vertices_not_total_dominating_set_of_star(self):
        G = gp.star_graph(3)
        for v in gp.nodes(G):
            for u in gp.nodes(G):
                if not gp.are_neighbors(G, u, v):
                    assert(gp.is_total_dominating_set(G, [u, v]) == False)
