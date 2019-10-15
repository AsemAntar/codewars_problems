import unittest
from count_binary import countBits


class TESTCOUNTBITS(unittest.TestCase):
    def test_count_bits(self):
        with self.subTest():
            self.assertEqual(countBits(1234), 5, 'should be 5')

        with self.subTest():
            self.assertEqual(countBits(0), 0, 'should be 0')

        with self.subTest():
            self.assertEqual(countBits(1), 1, 'should be 1')

        with self.subTest():
            self.assertEqual(countBits(4), 1, 'should be 1')

        with self.subTest():
            self.assertEqual(countBits(55), 5, 'should be 5')

        with self.subTest():
            self.assertEqual(countBits(987654321), 17, 'should be 17')

        with self.subTest():
            self.assertEqual(countBits(9), 2, 'should be 2')


if __name__ == '__main__':
    unittest.main()
