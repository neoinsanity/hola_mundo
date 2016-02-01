"""Module to produce translations of 'mundo'.

ElMundo
========

*ElMundo* is a great way to get translations for `Mundo`.
"""
import random

from hola_mundo.util import config_loader


class ElMundo(object):
    """Class that produces a random language version of 'mundo'."""

    def __init__(self):
        """Initialize Mundo from a resource file.

        :return: Nothing is returned.
        """
        self._mundos = config_loader.get_config('mundo')
        self._len = len(self._mundos)

    def mundo(self, index: int = None) -> str:
        """Method to retrieve a language version of 'mundo'.

        :param index: An optional index key to retrieve a given 'mundo'
            translation. If no index is set, then a random translation of
            world is returned.
        :return: A language version of 'mundo'.
        :except: IndexError - Thrown if there is no language translation for
            the given index.
        """
        if index is not None:
            if index > self._len:
                raise IndexError('There is no Mundo for index %s' % index)

            return self._mundos[index]
        else:
            return self._mundos[random.randint(0, self._len - 1)]
