import math

import pytest

import grinpy as gp


class TestTopologicalIndices:
    @pytest.mark.parametrize(
        "graph, expected_value",
        ((gp.path_graph(2), 1 ** -0.5), (gp.cycle_graph(3), 1.5), (gp.cycle_graph(4), 2), (gp.cycle_graph(5), 2.5)),
    )
    def test_randic_index(self, graph, expected_value):
        """Ensure randic_index returns the expected value for a given graph"""
        assert gp.randic_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, k, expected_value",
        (
            (gp.path_graph(2), -0.5, 1 ** -0.5),
            (gp.cycle_graph(3), -0.5, 1.5),
            (gp.cycle_graph(4), -0.5, 2),
            (gp.cycle_graph(5), -0.5, 2.5),
        ),
    )
    def test_generalized_randic_index(self, graph, k, expected_value):
        """Ensure randic_index returns the expected value for a given graph"""
        assert gp.generalized_randic_index(graph, k) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value", ((gp.path_graph(2), 1), (gp.cycle_graph(3), 1.5), (gp.complete_graph(4), 2))
    )
    def test_augmented_randic_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.augmented_randic_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value", ((gp.path_graph(2), 1), (gp.cycle_graph(3), 1.5), (gp.complete_graph(4), 2))
    )
    def test_harmonic_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.harmonic_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value",
        ((gp.path_graph(2), 0), (gp.cycle_graph(3), 3 * math.sqrt(2) / 2), (gp.complete_graph(4), 4.0)),
    )
    def test_atom_bond_connectivity_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.atom_bond_connectivity_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value",
        ((gp.path_graph(2), 1 / math.sqrt(2)), (gp.cycle_graph(3), 1.5), (gp.complete_graph(4), 6 / math.sqrt(6))),
    )
    def test_sum_connectivity_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.sum_connectivity_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value", ((gp.path_graph(2), 2.0), (gp.cycle_graph(3), 12.0), (gp.complete_graph(4), 36.0))
    )
    def test_first_zagreb_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.first_zagreb_index(graph) == expected_value

    @pytest.mark.parametrize(
        "graph, expected_value", ((gp.path_graph(2), 1.0), (gp.cycle_graph(3), 12.0), (gp.complete_graph(4), 54.0))
    )
    def test_second_zagreb_index(self, graph, expected_value):
        """Ensure augmented_randic_index returns the expected value for a given graph"""
        assert gp.second_zagreb_index(graph) == expected_value
