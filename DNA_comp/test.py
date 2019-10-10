import unittest
from DNA_complement import DNA_strand, DNA_strand_better_sol


class TESTDNACOMPLEMENT(unittest.TestCase):
    def test_DNA_strand(self):
        with self.subTest():
            self.assertEqual(DNA_strand('AAAA'), 'TTTT', 'Should Be TTTT')

        with self.subTest():
            self.assertEqual(DNA_strand('ATAT'), 'TATA', 'Should Be TATA')

        with self.subTest():
            self.assertEqual(DNA_strand('TACGATGCTTTAAA'),
                             'ATGCTACGAAATTT', 'Should Be ATGCTACGAAATTT')

    def test_DNA_strand_better_sol(self):
        with self.subTest():
            self.assertEqual(DNA_strand_better_sol(
                'AAAA'), 'TTTT', 'Should Be TTTT')

        with self.subTest():
            self.assertEqual(DNA_strand_better_sol(
                'ATAT'), 'TATA', 'Should Be TATA')

        with self.subTest():
            self.assertEqual(DNA_strand_better_sol('TACGATGCTTTAAA'),
                             'ATGCTACGAAATTT', 'Should Be ATGCTACGAAATTT')


if __name__ == '__main__':
    unittest.main()
