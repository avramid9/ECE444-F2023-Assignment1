import unittest
import utils

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        Utils = utils.Utils
        with self.assertRaises(ValueError):
            Utils.reversed("Hello")
        with self.assertRaises(ValueError):
            Utils.reversed(12.34)
        self.assertEqual(Utils.reversed(1234), 4321)

    def test_formatter(self):
        Utils = utils.Utils
        with self.assertRaises(TypeError):
            Utils.formatter("Hello")
        with self.assertRaises(TypeError):
            Utils.formatter(12.34)
        self.assertEqual(Utils.reversed(1234), 4321)


if __name__ == '__main__':
    unittest.main()