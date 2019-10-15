import unittest
from multiple_of_3_or_5 import solutions, solution, math_solution


class TESTSOLUTIONS(unittest.TestCase):
    def test_solutions(self):
        with self.subTest():
            self.assertEqual(solutions(10), 23, 'should be 23')
        with self.subTest():
            self.assertEqual(solutions(11), 33, 'should be 33')
        with self.subTest():
            self.assertEqual(solutions(16), 60, 'should be 60')
        with self.subTest():
            self.assertEqual(solutions(26), 168, 'should be 168')

    def test_solution(self):
        with self.subTest():
            self.assertEqual(solution(10), 23, 'should be 23')
        with self.subTest():
            self.assertEqual(solution(11), 33, 'should be 33')
        with self.subTest():
            self.assertEqual(solution(16), 60, 'should be 60')
        with self.subTest():
            self.assertEqual(solution(26), 168, 'should be 168')

    def test_math_solution(self):
        with self.subTest():
            self.assertEqual(math_solution(10), 23, 'should be 23')
        with self.subTest():
            self.assertEqual(math_solution(11), 33, 'should be 33')
        with self.subTest():
            self.assertEqual(math_solution(16), 60, 'should be 60')
        with self.subTest():
            self.assertEqual(math_solution(26), 168, 'should be 168')


if __name__ == '__main__':
    unittest.main()
