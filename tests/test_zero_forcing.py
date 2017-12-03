from grinpy import grinpy as gp

class TestZeroForcing():
    def test_leaf_is_zero_forcing_vertex_for_star(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_vertex(G, 1, 1) == True)

    def test_center_is_not_zero_forcing_vertex_for_star(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_vertex(G, 0, 0) == False)

    def test_no_vertex_is_zero_forcing_vertex_for_empty_set(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_vertex(G, 0, set()) == False)
        assert(gp.is_zero_forcing_vertex(G, 1, set()) == False)
        assert(gp.is_zero_forcing_vertex(G, 2, set()) == False)

    def test_center_of_S3_is_3_forcing_vertex(self):
        G = gp.star_graph(3)
        assert(gp.is_k_forcing_vertex(G, 0, 0, 3) == True)

    def test_center_of_S3_is_not_2_forcing_vertex(self):
        G = gp.star_graph(3)
        assert(gp.is_k_forcing_vertex(G, 0, 0, 2) == False)

    def test_leaf_of_star_is_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_active_set(G, 1) == True)

    def test_center_of_star_is_not_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_active_set(G, 0) == False)

    def test_empy_set_is_not_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert(gp.is_zero_forcing_active_set(G, set()) == False)

    def test_leaf_is_zero_forcing_set_of_path(self):
        G = gp.path_graph(3)
        assert(gp.is_zero_forcing_set(G, 0) == True)

    def test_leaf_is_not_zero_forcing_set_of_S3(self):
        G = gp.star_graph(3)
        assert(gp.is_zero_forcing_set(G, 1) == False)

    def test_leaf_is_max_degree_minus_one_forcing_set_for_star(self):
        for i in range(3, 13):
            G = gp.star_graph(i)
            D = gp.max_degree(G)
            assert(gp.is_k_forcing_set(G, 1, D-1) == True)

    def test_zero_forcing_number_of_star_is_order_minus_2(self):
        for i in range(2, 12):
            G = gp.star_graph(i)
            assert(gp.zero_forcing_number(G) == G.order() - 2)

    def test_zero_forcing_number_of_petersen_graph_is_5(self):
        G = gp.petersen_graph()
        assert(gp.zero_forcing_number(G) == 5)

    def test_2_forcing_number_of_petersen_graph_is_2(self):
        G = gp.petersen_graph()
        assert(gp.k_forcing_number(G, 2) == 2)
