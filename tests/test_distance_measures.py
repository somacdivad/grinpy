import pytest

import grinpy as gp


class TestDistanceMeasures:
    @pytest.mark.parametrize(
        "graph, expected_value",
        (
            (gp.cycle_graph(3), 3),
            (gp.cycle_graph(4), 4),
            (gp.cycle_graph(5), 5),
            (gp.path_graph(3), 4),
            (gp.path_graph(4), 6),
            (gp.path_graph(5), 8),
        ),
    )
    def test_triameter(self, graph, expected_value):
        """Ensure triameter returns the expected value for a given graph"""
        assert gp.triameter(graph) == expected_value
