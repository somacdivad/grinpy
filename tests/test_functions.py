import pytest

import grinpy as gp


class TestFunctions:
    def test_sequence_of_zeros_is_graphic(self):
        assert gp.is_graphic([0, 0, 0, 0]) == True

    def test_descending_sequence_of_integers_is_not_graphic(self):
        assert gp.is_graphic([5, 4, 3, 2, 1]) == False

    def test_elimination_sequence_of_complete_graph(self):
        G = gp.complete_graph(5)
        assert gp.elimination_sequence(G) == [4, 3, 2, 1, 0]

    @pytest.mark.parametrize(
        "graph, source, target, expected_value",
        (
            (gp.path_graph(5), 0, 4, 4),
            (gp.path_graph(5), 1, 4, 3),
            (gp.path_graph(5), 2, 4, 2),
            (gp.path_graph(5), 3, 4, 1),
            (gp.path_graph(5), 4, 4, 0),
        ),
    )
    def test_distance(self, graph, source, target, expected_value):
        """Ensure that distance returns the expected value for a given graph"""
        assert gp.distance(graph, source, target) == expected_value
