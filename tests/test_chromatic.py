import grinpy as gp


def test_chromatic_number_of_complete_graph_is_order():
    for i in range(1, 11):
        G = gp.complete_graph(i)
        assert gp.chromatic_number(G, method="ram-rama") == G.order()
        assert gp.chromatic_number(G, method="ilp") == G.order()


def test_chromatic_number_of_petersen_graph_is_3():
    G = gp.petersen_graph()
    assert gp.chromatic_number(G, method="ram-rama") == 3
    assert gp.chromatic_number(G, method="ilp") == 3
