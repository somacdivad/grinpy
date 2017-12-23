from grinpy import grinpy as gp

class TestIndependence():
    def test_single_vertex_is_independent_set(self):
        G = gp.trivial_graph()
        assert(gp.is_independent_set(G, [0]) == True)

    def test_single_vertex_is_2_independent_set(self):
        G = gp.trivial_graph()
        assert(gp.is_k_independent_set(G, [0], 2) == True)

    def test_set_of_leaves_of_star_is_independent_set(self):
        for i in range(2, 10):
            G = gp.star_graph(i)
            I = set(j for j in range(1, i+1))
            assert(gp.is_independent_set(G, I) == True)

    def test_empty_set_is_independent_set_of_trivial_graph(self):
        G = gp.trivial_graph()
        assert(gp.is_independent_set(G, set()) == True)

    def test_adjacent_vertices_of_star_is_not_independent_set(self):
        G = gp.star_graph(3)
        assert(gp.is_independent_set(G, [0, 1]) == False)
        assert(gp.is_independent_set(G, [0, 2]) == False)

    def test_set_of_leaves_of_star_is_2_independent_set(self):
        for i in range(2, 10):
            G = gp.star_graph(i)
            I = set(j for j in range(1, i+1))
            assert(gp.is_k_independent_set(G, I, 2) == True)

    def test_empty_set_is_2_independent_set_of_trivial_graph(self):
        G = gp.trivial_graph()
        assert(gp.is_k_independent_set(G, set(), 2) == True)

    def test_center_and_two_leaves_of_star_is_not_2_independent_set(self):
        G = gp.star_graph(3)
        assert(gp.is_independent_set(G, [0, 1, 2]) == False)

    def test_independence_number_of_complete_graph_is_1(self):
        for i in range(1, 13):
            G = gp.complete_graph(i)
            assert(gp.independence_number(G) == 1)

    def test_independence_number_of_star_is_order_minus_1(self):
        for i in range(1, 10):
            G = gp.star_graph(i)
            assert(gp.independence_number(G) == G.order() - 1)

    def test_2_independence_number_of_trivial_graph_is_1(self):
        G = gp.trivial_graph()
        assert(gp.k_independence_number(G, 2) == 1)

    def test_2_independence_number_of_complete_graph_is_2(self):
        for i in range(2, 11):
            G = gp.complete_graph(i)
            assert(gp.k_independence_number(G, 2) == 2)

    def test_2_independence_number_of_C5_is_3(self):
        G = gp.cycle_graph(5)
        assert(gp.k_independence_number(G, 2) == 3)

    def test_max_independent_set_of_empty_graph_is_all_nodes(self):
        for i in range(1, 11):
            G = gp.empty_graph(i)
            assert(gp.max_independent_set(G) == list(gp.nodes(G)))
