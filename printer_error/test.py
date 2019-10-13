import unittest
from printer_error import printer_error, printerError


class TESTPRINTERERROR(unittest.TestCase):
    def test_printer_error(self):
        with self.subTest():
            self.assertEqual(printer_error("aaabbbbhaijjjm"),
                             '0/14', 'should be 0/14')

        with self.subTest():
            self.assertEqual(printer_error(
                "aaaxbbbbyyhwawiwjjjwwm"), '8/22', 'should be 8/22')

        with self.subTest():
            self.assertEqual(printer_error(
                "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), '3/56', 'should be 3/56')

        with self.subTest():
            self.assertEqual(printer_error("mnopqrstuvwxyz"),
                             '13/14', 'should be 13/14')

        with self.subTest():
            self.assertEqual(printer_error("abcdefghijklm"),
                             '0/13', 'should be 0/13')

        with self.subTest():
            self.assertEqual(printer_error("nopqrstuvwxyz"),
                             '13/13', 'should be 13/13')

    def test_printerError(self):
        with self.subTest():
            self.assertEqual(printerError("aaabbbbhaijjjm"),
                             '0/14', 'should be 0/14')

        with self.subTest():
            self.assertEqual(printerError(
                "aaaxbbbbyyhwawiwjjjwwm"), '8/22', 'should be 8/22')

        with self.subTest():
            self.assertEqual(printerError(
                "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), '3/56', 'should be 3/56')

        with self.subTest():
            self.assertEqual(printerError("mnopqrstuvwxyz"),
                             '13/14', 'should be 13/14')

        with self.subTest():
            self.assertEqual(printerError("abcdefghijklm"),
                             '0/13', 'should be 0/13')

        with self.subTest():
            self.assertEqual(printerError("nopqrstuvwxyz"),
                             '13/13', 'should be 13/13')


if __name__ == '__main__':
    unittest.main()
