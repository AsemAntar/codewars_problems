import unittest
from highest_and_lowest_number import high_and_low


class TESTHIGHESTANDLOWEST(unittest.TestCase):
    def test_high_and_low(self):
        with self.subTest():
            self.assertEqual(high_and_low("1 9 3 4 -5"),
                             '9 -5', 'should be 9 -5')

        with self.subTest():
            self.assertEqual(high_and_low("2 5 1 6 0 100"),
                             '100 0', 'should be 100 0')

        with self.subTest():
            self.assertEqual(high_and_low("1 2 3 4 5"),
                             '5 1', 'should be 5 1')

        with self.subTest():
            self.assertEqual(high_and_low("-5 -4 -3 -2 -1 0"),
                             '0 -5', 'should be 0 -5')

        with self.subTest():
            self.assertEqual(high_and_low("100 200 300 400 -1000"),
                             '400 -1000', 'should be 400 -1000')


if __name__ == '__main__':
    unittest.main()
