import unittest
from math_quiz import rndm_integer, rndm_operator, new_problem


class TestMathGame(unittest.TestCase):

    def test_rndm_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = rndm_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_rndm_operator(self):
        # Test if the function and retun the right operators.

        right_operators = {'+', '-', '*'}
        for _ in range(2000):
            op = rndm_operator()
            self.assertIn(op, right_operators, f"wrong operator generated: {op}")

    def test_create_problem(self):
            test_cases = [(7, 7, '+', '7 + 7', 14),(7, 7, '-', '7 - 7', 0),(7, 7, '*', '7 * 7', 49),
            (5, 2, '+', '5 + 2', 7),(5, 2, '-', '5 - 2', 3),(5, 2, '*', '5 * 2', 10)]

            for number1, number2, op, exp_stat, exp_result in test_cases:
                prb_stat, result = new_problem(number1, number2, op)
                self.assertEqual(prb_stat, exp_stat, f"Expected statement '{exp_stat}', but got '{prb_stat}'")
                self.assertEqual(result, exp_result, f"Expected result '{exp_result}', but got '{result}'")


if __name__ == "__main__":
    unittest.main()
