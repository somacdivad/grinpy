from grinpy import grinpy as gp

class TestFunctions():
    def test_sequence_of_zeros_is_graphic(self):
        assert(gp.is_graphic([0, 0, 0, 0]) == True)

    def test_descending_sequence_of_integers_is_not_graphic(self):
        assert(gp.is_graphic([5, 4, 3, 2, 1]) == False)

    def test_elimination_sequence_of_complete_graph(self):
        G = gp.complete_graph(5)
        assert(gp.elimination_sequence(G) == [4, 3, 2, 1, 0])
