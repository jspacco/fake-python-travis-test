import unittest
from unnecessary_math import multiply


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_numbers_0_1(self):
        self.assertEqual(multiply(0, 1), 0)

    def test_numbers_1_2(self):
        self.assertEqual(multiply(1, 2), 2)


if __name__ == '__main__':
    unittest.main()