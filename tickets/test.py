import unittest
from tickets import tickets


class TESTTICKETS(unittest.TestCase):
    def test_tickets(self):
        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 25]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([50, 25, 25, 100]), 'NO')

        with self.subTest():
            self.assertEqual(tickets([25, 50]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 100]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 50, 100]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 50, 50, 100]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 25, 50, 50, 50, 100]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 50, 50, 50, 100]), 'NO')

        with self.subTest():
            self.assertEqual(tickets([50]), 'NO')

        with self.subTest():
            self.assertEqual(tickets([25]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([100]), 'NO')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 25, 50, 100]), 'YES')

        with self.subTest():
            self.assertEqual(tickets([25, 25, 25, 25, 50, 100, 100]), 'NO')


if __name__ == '__main__':
    unittest.main()
