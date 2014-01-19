"""Module to produce translations of 'mundo'.

ElMundo
========

*ElMundo* is a great way to get translations for `Mundo`.
"""
import random

from util import config_loader


class ElMundo(object):
    """Class that produces a random language version of 'mundo'."""

    def __init__(self):
        """Initialize Mundo from a resource file.

        :return: Nothing is returned.
        :rtype: None
        """
        self._mundos = config_loader.get_config('mundo')
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
