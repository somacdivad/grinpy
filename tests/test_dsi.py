import grinpy as gp
from math import ceil, floor
import pytest


class TestDSI:
    def test_non_integral_value_for_k_raises_TypeError(self):
        with pytest.raises(TypeError):
            G = gp.star_graph(2)
            gp.sub_k_domination_number(G, 1.5)

    def test_zero_value_for_k_raises_ValueError(self):
        with pytest.raises(ValueError):
            G = gp.star_graph(2)
            gp.sub_k_domination_number(G, 0)

    def test_integral_float_for_k_works(self):
        G = gp.star_graph(2)
        assert gp.sub_k_domination_number(G, 1.0) == 1

    def test_slater_of_complete_graph_is_1(self):
        for i in range(1, 10):
            G = gp.complete_graph(i)
            assert gp.slater(G) == 1

    def test_slater_of_cycle_is_third_of_nodes(self):
        for i in range(3, 13):
            G = gp.cycle_graph(i)
            assert gp.slater(G) == ceil(G.order() / 3)

    def test_sub_2_domination_number_of_complete_graph(self):
        for i in range(1, 10):
            G = gp.complete_graph(i)
            n = G.order()
            val = n / (1 + (0.5 * (n - 1)))
            assert gp.sub_k_domination_number(G, 2) == ceil(val)

    def test_sub_2_domination_number_of_cycle_is_half_of_nodes(self):
        for i in range(3, 13):
            G = gp.cycle_graph(i)
            assert gp.sub_k_domination_number(G, 2) == ceil(G.order() / 2)

    def test_sub_total_domination_number_of_complete_graph_is_2(self):
        for i in range(2, 10):
            G = gp.complete_graph(i)
            assert gp.sub_total_domination_number(G) == 2

    def test_sub_total_domination_number_of_empty_graph_is_None(self):
        for i in range(1, 9):
            G = gp.empty_graph(i)
            assert gp.sub_total_domination_number(G) == None

    def test_sub_total_domination_number_of_cycle_is_half_of_nodes(self):
        for i in range(3, 13):
            G = gp.cycle_graph(i)
            assert gp.sub_total_domination_number(G) == ceil(G.order() / 2)

    def test_annihilation_number_of_trivial_graph_is_1(self):
        G = gp.trivial_graph()
        assert gp.annihilation_number(G) == 1

    def test_annihilation_number_of_complete_graph_is_half_of_nodes(self):
        for i in range(2, 11):
            G = gp.complete_graph(i)
            assert gp.annihilation_number(G) == floor(G.order() / 2)

    def test_annihilation_number_of_star_is_order_minus_1(self):
        for i in range(2, 11):
            G = gp.star_graph(i)
            assert gp.annihilation_number(G) == G.order() - 1
