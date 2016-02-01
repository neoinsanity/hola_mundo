"""An example of a basic unit test file setup."""

import unittest


class HolaMundoTest(unittest.TestCase):
    """The simplest unit test case class."""

    def setUp(self):
        """Overrides the unittest.TestCase for environment setup."""
        super(HolaMundoTest, self).setUp()

    def tearDown(self):
        """Overrides the unittest.TestCase for environment tear down."""
        super(HolaMundoTest, self).tearDown()

    def a_test(self):

        """Wow, a test that runs."""
        self.assertTrue(True)
