import grinpy as gp
import pytest


class TestZeroForcing:
    def test_non_integral_value_for_k_raises_TypeError_in_is_k_forcing(self):
        with pytest.raises(TypeError):
            G = gp.star_graph(2)
            gp.is_k_forcing_vertex(G, 1, [1], 1.5)

    def test_0_value_for_k_raises_ValueError_in_is_k_forcing(self):
        with pytest.raises(ValueError):
            G = gp.star_graph(2)
            gp.is_k_forcing_vertex(G, 1, [1], 0)

    def test_integral_float_for_k_works(self):
        G = gp.star_graph(2)
        assert gp.is_k_forcing_vertex(G, 1, [1], 1.0) == True

    def test_leaf_is_zero_forcing_vertex_for_star(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_vertex(G, 1, [1]) == True

    def test_center_is_not_zero_forcing_vertex_for_star(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_vertex(G, 0, [0]) == False

    def test_no_vertex_is_zero_forcing_vertex_for_empty_set(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_vertex(G, 0, set()) == False
        assert gp.is_zero_forcing_vertex(G, 1, set()) == False
        assert gp.is_zero_forcing_vertex(G, 2, set()) == False

    def test_center_of_S3_is_3_forcing_vertex(self):
        G = gp.star_graph(3)
        assert gp.is_k_forcing_vertex(G, 0, [0], 3) == True

    def test_center_of_S3_is_not_2_forcing_vertex(self):
        G = gp.star_graph(3)
        assert gp.is_k_forcing_vertex(G, 0, [0], 2) == False

    def test_leaf_of_star_is_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_active_set(G, [1]) == True

    def test_center_of_star_is_not_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_active_set(G, [0]) == False

    def test_empy_set_is_not_zero_forcing_active_set(self):
        G = gp.star_graph(2)
        assert gp.is_zero_forcing_active_set(G, set()) == False

    def test_leaf_is_zero_forcing_set_of_path(self):
        G = gp.path_graph(3)
        assert gp.is_zero_forcing_set(G, [0]) == True

    def test_leaf_is_not_zero_forcing_set_of_S3(self):
        G = gp.star_graph(3)
        assert gp.is_zero_forcing_set(G, [1]) == False

    def test_leaf_is_max_degree_minus_one_forcing_set_for_star(self):
        for i in range(3, 13):
            G = gp.star_graph(i)
            D = gp.max_degree(G)
            assert gp.is_k_forcing_set(G, [1], D - 1) == True

    def test_zero_forcing_number_of_star_is_order_minus_2(self):
        for i in range(2, 12):
            G = gp.star_graph(i)
            assert gp.zero_forcing_number(G) == G.order() - 2

    def test_zero_forcing_number_of_petersen_graph_is_5(self):
        G = gp.petersen_graph()
        assert gp.zero_forcing_number(G) == 5

    def test_2_forcing_number_of_petersen_graph_is_2(self):
        G = gp.petersen_graph()
        assert gp.k_forcing_number(G, 2) == 2

    def test_leaf_is_not_total_forcing_set_of_path(self):
        G = gp.path_graph(3)
        assert gp.is_total_zero_forcing_set(G, [0]) == False

    def test_pair_of_adjacent_nodes_is_total_forcing_set_of_path(self):
        G = gp.path_graph(6)
        assert gp.is_total_zero_forcing_set(G, [2, 3]) == True

    def test_total_zero_forcing_number_of_path_is_2(self):
        G = gp.path_graph(5)
        assert gp.total_zero_forcing_number(G) == 2

    def test_connected_zero_forcing_number_of_monster_is_4(self):
        G = gp.star_graph(3)
        G.add_edge(3, 4)
        G.add_edge(3, 5)
        assert gp.connected_zero_forcing_number(G) == 4

    def test_non_int_value_for_k_raises_error_in_is_connected_k_forcing(self):
        with pytest.raises(TypeError):
            G = gp.star_graph(2)
            gp.is_connected_k_forcing_set(G, [0], 1.5)

    def test_0_value_for_k_raises_error_in_is_connected_k_forcing(self):
        with pytest.raises(ValueError):
            G = gp.star_graph(2)
            gp.is_connected_k_forcing_set(G, [0], 0)

    def test_non_int_value_for_k_raises_error_in_min_connected_k_forcing(self):
        with pytest.raises(TypeError):
            G = gp.star_graph(2)
            gp.min_connected_k_forcing_set(G, 1.5)

    def test_0_value_for_k_raises_error_in_min_connected_k_forcing(self):
        with pytest.raises(ValueError):
            G = gp.star_graph(2)
            gp.min_connected_k_forcing_set(G, 0)

    def test_non_int_value_for_k_raises_error_in_connected_k_forcing_num(self):
        with pytest.raises(TypeError):
            G = gp.star_graph(2)
            gp.connected_k_forcing_number(G, 1.5)

    def test_0_value_for_k_raises_error_in_connected_k_forcing_num(self):
        with pytest.raises(ValueError):
            G = gp.star_graph(2)
            gp.connected_k_forcing_number(G, 0)

    def test_total_zero_forcing_num_of_trivial_graph_is_None(self):
        G = gp.trivial_graph()
        assert gp.total_zero_forcing_number(G) == None

    def test_endpoint_is_connected_forcing_set_of_path(self):
        G = gp.path_graph(2)
        assert gp.is_connected_zero_forcing_set(G, [0])

    def test_connected_zero_forcing_num_of_disconnected_graph_is_None(self):
        G = gp.empty_graph(5)
        assert gp.connected_zero_forcing_number(G) == None
