# -*- coding: utf-8 -*-

#    Copyright (C) 2017-2019 by
#    David Amos <somacdivad@gmail.com>
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: David Amos <somacdivad@gmail.com>
#          Randy Davila <davilar@uhd.edu>
"""HavelHakimi class from performing and keeping track of the Havel Hakimi
Process on a sequence."""

from collections.abc import Iterable

from grinpy.utils import contains_only_zeros


class HavelHakimi:
    """Class for performing and keeping track of the Havel Hakimi process on a
    sequence of positive integers.

    Parameters
    ----------
    sequence : input sequence
        The sequence of integers to initialize the Havel Hakimi process.
    """

    def __init__(self, sequence):
        if not isinstance(sequence, Iterable):
            raise TypeError("`sequence` must iterable")

        for x in sequence:
            if not float(x).is_integer():
                raise TypeError("Sequence must contain only integers.")
        # make sure all entries in the sequence are of type int and sort in non-increasing order
        S = [int(x) for x in sequence]
        S.sort(reverse=True)
        process_sequence = [list(S)]  # keeps track of resulting sequences at each step
        elim_sequence = []  # keeps track of the elements eliminated at each step
        while S[0] > 0 and S[0] < len(S):
            # so long as the largest element d of the sequence is positive, remove d from the sequence and subtract 1 from the next d elements
            d = S.pop(0)
            for i in range(d):
                S[i] = S[i] - 1
            S.sort(reverse=True)
            # append the resulting sequence to the process sequence
            process_sequence.append(list(S))
            # append the removed element to the elimination sequence
            elim_sequence.append(d)
        # finally, append the 0s in the last step of the Havel Hakimi process to the elimination sequence
        if contains_only_zeros(process_sequence[-1]):
            elim_sequence.extend(S)
        # set class attributes
        self.process = process_sequence
        self.eliminationSequence = elim_sequence

    def depth(self):
        """Return the depth of the Havel Hakimi process.

        Returns
        -------
        int
            The depth of the Havel Hakimi process.
        """
        return len(self.process) - 1

    def get_elimination_sequence(self):
        """Return the elimination sequence of the Havel Hakimi process.

        Returns
        -------
        list
            The elimination sequence of the Havel Hakimi process.
        """
        return self.eliminationSequence

    def get_initial_sequence(self):
        """Return the initial sequence passed to the Havel Hakimi class for
        initialization.

        Returns
        -------
        list
            The initial sequence passed to the Havel Hakimi class.
        """
        return self.process[0]

    def is_graphic(self):
        """Return whether or not the initial sequence is graphic.

        Returns
        -------
        bool
            True if the initial sequence is graphic. False otherwise.
        """
        return contains_only_zeros(self.process[-1])

    def get_process(self):
        """Return the list of sequence produced during the Havel Hakimi process.
        The first element in the list is the initial sequence.

        Returns
        -------
        list
            The list of sequences produced by the Havel Hakimi process.
        """
        return self.process

    def residue(self):
        """Return the residue of the sequence.

        Returns
        -------
        int
            The residue of the initial sequence. If the sequence is not graphic,
            this will be None.
        """
        return len(self.process[-1]) if self.is_graphic() else None
