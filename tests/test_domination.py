import grinpy as gp
import pytest


def test_non_integral_value_for_k_raises_error_in_is_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.is_k_dominating_set(G, [0], 1.5)


def test_0_value_for_k_raises_error_in_is_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.is_k_dominating_set(G, [0], 0)


def test_non_int_value_for_k_raises_error_in_min_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.min_k_dominating_set(G, 1.5)


def test_0_value_for_k_raises_error_in_min_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.min_k_dominating_set(G, 0)


def test_non_int_value_for_k_raises_error_in_k_dom_num():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.k_domination_number(G, 1.5)


def test_0_value_for_k_raises_error_in_k_dom_num():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.k_domination_number(G, 0)


def test_integral_float_for_k_works():
    G = gp.star_graph(2)
    assert gp.is_k_dominating_set(G, [0], 1.0) is True


def test_max_degree_vertex_is_dominating_set_of_star():
    for i in range(1, 9):
        G = gp.star_graph(i)
        assert gp.is_k_dominating_set(G, [0], 1) is True


def test_min_degree_vertex_is_not_dominating_set_of_star():
    for i in range(2, 9):
        G = gp.star_graph(i)
        assert gp.is_k_dominating_set(G, [1], 1) is False


def test_dominating_set_with_nodes_not_in_graph():
    G = gp.star_graph(3)
    assert gp.is_k_dominating_set(G, [4], 1) is False
    assert gp.is_k_dominating_set(G, [0, 4], 1) is True


def test_max_degree_vertex_is_not_2_dominating_set_of_star():
    for i in range(1, 9):
        G = gp.star_graph(i)
        assert gp.is_k_dominating_set(G, [0], 2) is False


def test_min_degree_vertices_are_2_dominating_set_of_star():
    for i in range(2, 9):
        G = gp.star_graph(i)
        nodes = [i for i in range(1, i + 2)]
        assert gp.is_k_dominating_set(G, nodes, 2) is True


def test_2_dominating_set_with_nodes_not_in_graph():
    G = gp.star_graph(3)
    nodes = [1, 2, 3, 4]
    assert gp.is_k_dominating_set(G, [4], 1) is False
    assert gp.is_k_dominating_set(G, nodes, 1) is True


def test_no_single_node_is_total_dominating_set_of_star():
    G = gp.star_graph(3)
    for v in gp.nodes(G):
        assert gp.is_total_dominating_set(G, [v]) is False


def test_adjacent_vertices_are_total_dominating_set_of_star():
    G = gp.star_graph(3)
    for v in gp.nodes(G):
        for u in gp.nodes(G):
            if gp.are_neighbors(G, u, v):
                assert gp.is_total_dominating_set(G, [u, v]) is True


def test_non_adjacent_vertices_not_total_dominating_set_of_star():
    G = gp.star_graph(3)
    for v in gp.nodes(G):
        for u in gp.nodes(G):
            if not gp.are_neighbors(G, u, v):
                assert gp.is_total_dominating_set(G, [u, v]) is False


def test_center_vertex_of_star_is_connected_dominating_set():
    G = gp.star_graph(3)
    assert gp.is_connected_dominating_set(G, [0]) is True


def test_leaves_of_star_are_not_connected_dominating_set():
    G = gp.star_graph(3)
    D = [1, 2, 3]
    assert gp.is_connected_dominating_set(G, D) is False


def test_3_adjacent_vertice_is_connected_2_dominating_set_of_4_cycle():
    G = gp.cycle_graph(4)
    assert gp.is_connected_k_dominating_set(G, [0, 1, 2], 2) is True


def test_non_adjacent_vertices_not_connected_2_dom_set_of_4_cycle():
    G = gp.cycle_graph(4)
    assert gp.is_connected_k_dominating_set(G, [0, 2], 2) is False


def test_connected_domination_number_of_star_is_1():
    G = gp.star_graph(3)
    assert gp.connected_domination_number(G) == 1


def test_connected_domination_number_of_P5_is_3():
    G = gp.path_graph(5)
    assert gp.connected_domination_number(G) == 3


def leaves_of_star_is_independent_dominating_set():
    G = gp.star_graph(3)
    D = [1, 2, 3]
    assert gp.is_independent_dominating_set(G, D) is True


def center_node_and_leaf_is_not_ind_dom_set_of_star():
    G = gp.star_graph(3)
    assert gp.is_independent_dominating_set(G, [0, 1]) is False


def test_independent_domination_num_of_monster_is_3():
    G = gp.star_graph(3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    assert gp.independent_domination_number(G, method="bf") == 3
    assert gp.independent_domination_number(G, method="ilp") == 3


def test_non_int_value_for_k_raises_error_in_connected_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.is_connected_k_dominating_set(G, [0], 1.5)


def test_0_value_for_k_raises_error_in_connected_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.is_connected_k_dominating_set(G, [0], 0)


def test_non_int_value_for_k_raises_error_in_min_connected_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.min_connected_k_dominating_set(G, 1.5)


def test_0_value_for_k_raises_error_in_min_connected_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.min_connected_k_dominating_set(G, 0)


def test_non_int_value_for_k_raises_error_in_connected_k_dom_num():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.connected_k_domination_number(G, 1.5)


def test_0_value_for_k_raises_error_in_connected_k_dom_num():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.connected_k_domination_number(G, 0)


def test_non_int_value_for_k_raises_error_in_ind_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.is_independent_k_dominating_set(G, [0], 1.5)


def test_0_value_for_k_raises_error_in_ind_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.is_independent_k_dominating_set(G, [0], 0)


def test_non_int_value_for_k_raises_error_in_min_ind_k_dom_set():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.min_independent_k_dominating_set(G, 1.5)


def test_0_value_for_k_raises_error_in_min_ind_k_dom_set():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.min_independent_k_dominating_set(G, 0)


def test_min_ind_dom_set_ip_returns_same_as_bf_for_peterson_graph():
    G = gp.petersen_graph()
    bf = len(gp.min_independent_dominating_set(G, method="bf"))
    ip = len(gp.min_independent_dominating_set(G, method="ilp"))
    assert bf == ip


def test_non_int_value_for_k_raises_error_in_ind_k_dom_num():
    with pytest.raises(TypeError):
        G = gp.star_graph(2)
        gp.independent_k_domination_number(G, 1.5)


def test_0_value_for_k_raises_error_in_ind_k_dom_num():
    with pytest.raises(ValueError):
        G = gp.star_graph(2)
        gp.independent_k_domination_number(G, 0)


def test_min_conn_dominating_for_disconnected_graph_is_0():
    G = gp.Graph()
    G.add_edge(1, 2)
    G.add_edge(3, 4)
    assert gp.connected_domination_number(G) == 0


def test_tot_dom_for_graph_with_isolates_is_0():
    G = gp.empty_graph(5)
    assert gp.total_domination_number(G, method="bf") == 0
    assert gp.total_domination_number(G, method="ilp") == 0


def test_domination_number_of_star_is_1():
    for i in range(1, 9):
        G = gp.star_graph(i)
        assert gp.domination_number(G, method="bf") == 1
        assert gp.domination_number(G, method="ilp") == 1


def test_2_domination_number_of_star_is_order_minus_1():
    for i in range(2, 9):
        G = gp.star_graph(i)
        assert gp.k_domination_number(G, 2) == G.order() - 1


def test_total_domination_number_of_star_is_2():
    for i in range(1, 9):
        G = gp.star_graph(i)
        assert gp.total_domination_number(G, method="bf") == 2
        assert gp.total_domination_number(G, method="ilp") == 2
