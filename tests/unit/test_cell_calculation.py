import unittest
import random
import math

from matrix_multiplication.commands import CalculateMatrixCellValueCommand


class TestCellCalculation(unittest.TestCase):
    """This test case checks if the calculation of any matrix cell works correctly
    """
    def test_calculation(self):
        n = random.randint(10, 20)
        row = [random.random() for i in range(0, n)]
        column = [random.random() for i in range(0, n)]
        command = CalculateMatrixCellValueCommand(row=row, column=column)
        expected_value = sum([row[i] * column[i] for i in range(0, n)])
        self.assertAlmostEqual(expected_value, command.__call__())

if __name__ == "__main__":
    unittest.main()
