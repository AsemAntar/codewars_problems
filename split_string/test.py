import unittest
from split_string import solution


class TestSolution(unittest.TestCase):
    tests = (
        ("abcdef", ['ab', 'cd', 'ef']),
        ("abc", ['ab', 'c_']),
        ("", []),
        ("x", ['x_'])
    )

    def test_solution(self):
        for inp, exp in self.tests:
            self.assertEqual(solution(inp), exp)


if __name__ == '__main__':
    unittest.main()
