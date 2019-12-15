import unittest
from is_prime import is_prime


class TESTISPRIME(unittest.TestCase):
    def test_is_prime(self):
        with self.subTest():
            self.assertEqual(is_prime(1), False)
        with self.subTest():
            self.assertEqual(is_prime(2), True)
        with self.subTest():
            self.assertEqual(is_prime(3), True)
        with self.subTest():
            self.assertEqual(is_prime(0), False)
        with self.subTest():
            self.assertEqual(is_prime(-1), False)


if __name__ == '__main__':
    unittest.main()
