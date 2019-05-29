import grinpy as gp


def test_min_vertex_cover():
    G = gp.empty_graph()
    assert isinstance(gp.min_vertex_cover(G, method="ilp"), set)


def test_vertex_cover_of_null_graph():
    G = gp.empty_graph()
    assert gp.min_vertex_cover(G, method="ilp") == set()
    assert gp.vertex_cover_number(G) == 0


def test_vertex_cover_of_empty_graph():
    G = gp.empty_graph(4)
    assert gp.vertex_cover_number(G) == 0


def test_vertex_cover_number_of_K4_is_3():
    G = gp.complete_graph(4)
    assert gp.vertex_cover_number(G) == 3
