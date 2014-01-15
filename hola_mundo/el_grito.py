"""Random salutation generator..

"""
import os
import random


class ElGrito(object):
    """Class that produces a random language version of 'hola'."""

    def __init__(self):
        """Initialize ElGrito from a resource file.

        :return: Nothing is returned.
        :rtype: None
        """
        current_dir = os.path.dirname(__file__)
        grito_file = os.path.join(current_dir, 'resources', 'grito.txt')

        self._gritos = list()
        with open(grito_file) as f:
            for line in f:
                self._gritos.append(line.strip())
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
