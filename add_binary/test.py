import unittest
from add_binary import add_binary


class TESTADDBINARY(unittest.TestCase):
    def test_add_binary(self):
        with self.subTest():
            self.assertEqual(add_binary(1, 1), '10', 'should be 10')
        with self.subTest():
            self.assertEqual(add_binary(1, 0), '1', 'should be 1')
        with self.subTest():
            self.assertEqual(add_binary(0, 1), '1', 'should be 1')
        with self.subTest():
            self.assertEqual(add_binary(2, 2), '100', 'should be 100')
        with self.subTest():
            self.assertEqual(add_binary(51, 12), '111111', 'should be 111111')
        with self.subTest():
            self.assertEqual(add_binary(43, 60), '1100111',
                             'should be 1100111')


if __name__ == '__main__':
    unittest.main()
