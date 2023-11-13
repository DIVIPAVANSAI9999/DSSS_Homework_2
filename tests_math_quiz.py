import unittest
from math_quiz import new_function_A, new_function_B, new_function_C


class TestMathQuizFunctions(unittest.TestCase):

    def test_new_function_A(self):
        result = new_function_A(2, 3)
        self.assertEqual(result, 5, "Error: new_function_A did not return the expected result.")

    def test_new_function_B(self):
        result = new_function_B(4, 2)
        self.assertEqual(result, 8, "Error: new_function_B did not return the expected result.")

    def test_new_function_C(self):
        result = new_function_C(5, 2)
        self.assertEqual(result, 10, "Error: new_function_C did not return the expected result.")


if __name__ == '__main__':
    unittest.main()