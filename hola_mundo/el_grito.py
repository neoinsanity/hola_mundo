"""Module to produce translations of 'hola'.

ElGrito
========

*ElGrito* is a great way to get translations for 'Hola'.
"""
import random

from hola_mundo.util import config_loader


class ElGrito(object):
    """Class that produces a random language version of 'hola'."""

    def __init__(self):
        """Initialize ElGrito from a resource file.

        :return: Nothing is returned.
        """
        self._gritos = config_loader.get_config('grito')
        self._len = len(self._gritos)

    def grito(self, index: int = None) -> str:
        """Method to retrieve a language version of 'hola'.

        :param index: An optional index key to retrieve a given 'hola'
            translation. If no index key is provided, a random translation of
            hello is generated.
        :return: A language version of 'hola'.
        :except: IndexError - Thrown if there is no language translation for
            the given index.
        """
        if index is not None:
            if index > self._len:
                raise IndexError('There is no Hola for index %s' % index)
            return self._gritos[index]
        else:
            return self._gritos[random.randint(0, self._len - 1)]
