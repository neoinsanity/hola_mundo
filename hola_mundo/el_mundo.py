"""Module to produce translations of 'mundo'.

ElMundo
========

*ElMundo* is a great way to get translations for `Mundo`.
"""
import os
import random


class ElMundo(object):
    """Class that produces a random language version of 'mundo'."""

    def __init__(self):
        """Initialize Mundo from a resource file.

        :return: Nothing is returned.
        :rtype: None
        """
        current_dir = os.path.dirname(__file__)
        mundo_file = os.path.join(current_dir, 'resources', 'mundo.txt')

        self._mundos = list()
        with open(mundo_file) as f:
            for line in f:
                self._mundos.append(line.strip())
        self._len = len(self._mundos)

    def mundo(self, index=None):
        """Method to retrieve a language version of 'mundo'.

        :param index: An index key to retrieve a given 'mundo' translation.
        :type index: int
        :return: A language version of 'mundo'.
        :rtype: str
        """
        if index > self._len:
            raise IndexError('There is no Mundo for index %s' % index)

        if index is not None:
            return self._mundos[index]
        else:
            return self._mundos[random.randint(0, self._len - 1)]
