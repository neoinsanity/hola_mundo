"""Testing ElGrito class."""
import unittest

from hola_mundo.el_mundo import ElMundo


class ElMundoTest(unittest.TestCase):
    def setUp(self):
        self.el_mundo = ElMundo()

    def test_mundo_index(self):
        """Ensure that index feature works."""
        mundo = self.el_mundo.mundo(0)
        self.assertIsNotNone(mundo, 'Expected NOT None mundo.')
        self.assertEqual(mundo, 'Mundo', 'Unexpected mundo: %s' % mundo)

    def test_mundo_random(self):
        """Ensure randome feature works."""
        mundo = self.el_mundo.mundo()
        self.assertIsNotNone(mundo, 'Expected NOT None mundo.')

    def test_mundo_exception(self):
        """Test index out of bound exception"""
        self.assertRaises(IndexError, self.el_mundo.mundo, 10)


