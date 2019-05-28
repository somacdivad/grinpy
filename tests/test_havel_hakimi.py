import grinpy as gp
import pytest


class TestHavelHakimi:
    def test_non_integer_values_raises_TypeError(self):
        with pytest.raises(TypeError):
            hh = gp.HavelHakimi([3, 3, 1.5, 1])

    def test_non_iterable_raises_TypeError(self):
        with pytest.raises(TypeError):
            hh = gp.HavelHakimi(0)

    def test_havel_hakimi_with_integral_floats(self):
        hh = gp.HavelHakimi([1.0, 1.0])
        assert hh.residue() == 1

    def test_descending_sequence_of_integers_is_not_graphic(self):
        hh = gp.HavelHakimi([5, 4, 3, 2, 1])
        assert hh.is_graphic() == False

    def test_sequence_of_zeros_is_graphic(self):
        hh = gp.HavelHakimi([0, 0, 0, 0, 0])
        assert hh.is_graphic() == True

    def test_process_of_compete_graph(self):
        G = gp.complete_graph(4)
        hh = gp.HavelHakimi(gp.degree_sequence(G))
        p = [[3, 3, 3, 3], [2, 2, 2], [1, 1], [0]]
        assert hh.get_process() == p

    def test_elimination_sequence_of_complete_graph(self):
        G = gp.complete_graph(4)
        hh = gp.HavelHakimi(gp.degree_sequence(G))
        e = [3, 2, 1, 0]
        assert hh.get_elimination_sequence() == e

    def test_initial_sequence(self):
        G = gp.complete_graph(4)
        hh = gp.HavelHakimi(gp.degree_sequence(G))
        assert hh.get_initial_sequence() == [3, 3, 3, 3]

    def test_depth_of_complete_graph_is_order_minus_1(self):
        for i in range(2, 12):
            G = gp.complete_graph(i)
            hh = gp.HavelHakimi(gp.degree_sequence(G))
            assert hh.depth() == G.order() - 1
