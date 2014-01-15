"""Module to produce translations of 'mundo'.

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

        with open(mundo_file) as f:
            self._mundos = f.readlines()

    def mundo(self, index=None):
        """Method to retrieve a language version of 'mundo'.

        :param index: An index key to retrieve a given 'mundo' translation.
        :type index: int
        :return: A language version of 'mundo'.
        :rtype: str
        """
        if index is not None:
            return self._mundo[index]
        else:
            return self._mundos[random.randint(0, len(self._mundos) - 1)]
