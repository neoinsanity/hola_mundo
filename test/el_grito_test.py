"""Testing ElMundo class."""
import unittest

from hola_mundo.el_grito import ElGrito


class ElGritoTest(unittest.TestCase):
    def setUp(self):
        self.el_grito = ElGrito()

    def test_grito_index(self):
        """Ensure that index feature works."""
        grito = self.el_grito.grito(0)
        self.assertIsNotNone(grito, 'Expected NOT None grito.')
        self.assertEqual(grito, u'Hola', 'Unexpected grito: [%s]' % grito)

    def test_mundo_random(self):
        """Ensure random feature works."""
        grito = self.el_grito.grito()
        self.assertIsNotNone(grito, 'Expected NOT None grito.')

    def test_mundo_exception(self):
        """Test index out of bound exception."""
        self.assertRaises(IndexError, self.el_grito.grito, 10)
