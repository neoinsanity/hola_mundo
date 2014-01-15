"""Testing ElMundo class."""
import unittest

from hola_mundo.el_grito import ElGrito


class ElGritoTest(unittest.TestCase):
    def setUp(self):
        self.el_grito = ElGrito()

    def test_grito_index(self):
        grito = self.el_grito.grito(1)
        self.assertIsNotNone(grito, 'Expected NOT None grito.')
        self.assertEqual(grito, '', 'Unexpected grito: %s' % grito)

    def test_mundo_random(self):
        grito = self.el_grito.grito()
        self.assertIsNotNone(grito, 'Expected NOT None grito.')

    def test_mundo_exception(self):
        self.el_grito.grito(10)
