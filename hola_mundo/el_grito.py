import os
import random

__author__ = 'Raul Gonzalez'


class ElGrito(object):
    def __init__(self):
        current_dir = os.path.dirname(__file__)
        grito_file = os.path.join(current_dir, 'resources', 'grito.txt')

        with open(grito_file) as f:
            self._gritos = f.readlines()

    def grito(self):
        return self._gritos[random.randint(0, len(self._gritos) - 1)]
