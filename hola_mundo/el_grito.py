"""Random salutation generator..

"""
import random

from util import config_loader


class ElGrito(object):
    """Class that produces a random language version of 'hola'."""

    def __init__(self):
        """Initialize ElGrito from a resource file.

        :return: Nothing is returned.
        :rtype: None
        """
        self._gritos = config_loader.get_config('grito')
        self._len = len(self._gritos)

    def grito(self, index=None):
        """Method to retrieve a language version of 'hola'.

        :param index: An index key to retrieve a given 'hola' translation.
        :type index: int
        :return: A language version of 'hola'.
        :rtype: str
        """
        if index > self._len:
            raise IndexError('There is no Hola for index %s' % index)

        if index is not None:
            return self._gritos[index]
        else:
            return self._gritos[random.randint(0, self._len - 1)]
