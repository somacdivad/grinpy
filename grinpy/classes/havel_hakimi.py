# -*- coding: utf-8 -*-

#    Copyright (C) 2017 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""HavelHakimi class from performing and keeping track of the Havel Hakimi
Process on a sequence."""

from grinpy.utils import contains_only_zeros

class HavelHakimi:

    def __init__(self, lSequence):
        lSequence.sort(reverse = True)
        process_sequence = [list(lSequence)] # keeps track of resulting sequences at each step
        elim_sequence = [] # keeps track of the elements eliminated at each step
        while lSequence[0] > 0 and lSequence[0] < len(lSequence):
            # so long as the largest element d of the sequence is positive, remove d from the sequence and subtract 1 from the next d elements
            d = lSequence.pop(0)
            for i in range(d):
                lSequence[i] = lSequence[i] - 1
            lSequence.sort(reverse = True)
            # append the resulting sequence to the process sequence
            process_sequence.append(list(lSequence))
            # append the removed element to the elimination sequence
            elim_sequence.append(d)
        # finally, append the 0s in the last step of the Havel Hakimi process to the elimination sequence
        if contains_only_zeros(process_sequence[-1]):
            elim_sequence.extend(lSequence)
        # set class attributes
        self.process = process_sequence
        self.eliminationSequence =  elim_sequence

    def depth(self):
        return len(self.process) - 1

    def get_elimination_sequence(self):
        return self.eliminationSequence

    def get_initial_sequence(self):
        return self.process[0]

    def is_graphic(self):
        return contains_only_zeros(self.process[-1])

    def get_process(self):
        return self.process

    def residue(self):
        return len(self.process[-1]) if self.is_graphic() else 0
        # TODO: May be better to return False or None?
