import grinpy as gp

class TestChromatic():

    def test_chromatic_number_of_complete_graph_is_order(self):
        for i in range(1, 11):
            G = gp.complete_graph(i)
            assert(gp.chromatic_number(G) == G.order())

    def test_chromatic_number_of_petersen_graph_is_3(self):
        G = gp.petersen_graph()
        assert(gp.chromatic_number(G) == 3)
