import grinpy as gp
from math import ceil, floor


class TestPowerDomination:
    def test_center_node_is_power_dominating_set_of_star(self):
        for i in range(1, 11):
            G = gp.star_graph(i)
            assert gp.is_power_dominating_set(G, [0]) == True

    def test_leaf_is_not_power_dominating_set_of_star(self):
        for i in range(3, 13):
            G = gp.star_graph(i)
            for j in range(1, i + 1):
                assert gp.is_power_dominating_set(G, [j]) == False

    def test_empty_set_is_not_power_dominating_set_of_trivial_graph(self):
        G = gp.trivial_graph()
        assert gp.is_power_dominating_set(G, set()) == False

    def test_power_domination_number_of_complete_graph_is_1(self):
        for i in range(1, 11):
            G = gp.complete_graph(i)
            assert gp.power_domination_number(G) == 1

    def test_power_domination_number_of_barbell_is_2(self):
        for i in range(3, 13):
            G = gp.barbell_graph(i, i)
            assert gp.power_domination_number(G) == 2
