"""Testing ElGrito class."""
import unittest

from hola_mundo.el_mundo import ElMundo


class ElMundoTest(unittest.TestCase):
    def setUp(self):
        self.el_mundo = ElMundo()

    def test_mundo_index(self):
        mundo = self.el_mundo.mundo(1)
        self.assertIsNotNone(mundo, 'Expected NOT None mundo.')
        self.assertEqual(mundo, '', 'Unexpected mundo: %s' % mundo)

    def test_mundo_random(self):
        mundo = self.el_mundo.mundo()
        self.assertIsNotNone(mundo, 'Expected NOT None mundo.')

    def test_mundo_exception(self):
        self.el_mundo.mundo(10)


