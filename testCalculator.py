import unittest
from calculator import Calculator
from csvReader import CsvReader

class MyTestCase(unittest.TestCase): 
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader("Tests/Unit Test Addition.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.addRes(row['Value 1'], row['Value 2']), res)
            self.assertEqual(self.calculator.res, res)

    def test_division(self):
        test_data = CsvReader("Tests/Data/Unit Test Division.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.divRes(row['Value 2'], row['Value 1']), res)
            self.assertEqual(self.calculator.res, res)

    def test_multiplication(self):
        test_data = CsvReader("Tests/Data/Unit Test Multiplication.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.multRes(row['Value 1'], row['Value 2']), res)
            self.assertEqual(self.calculator.res, res)
	
    def test_squared(self):
        test_data = CsvReader("Tests/Data/Unit Test Square.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.squareRes(row['Value 1']), res)
            self.assertEqual(self.calculator.res, res)

    def test_squareRoot(self):
        test_data = CsvReader("Tests/Data/Unit Test Square Root.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.squareRootRes(row['Value 1']), round(res,8))
            self.assertEqual(self.calculator.res, round(res,8))

    def test_subtraction(self):
        test_data = CsvReader("Tests/Data/Unit Test Subtraction.csv").data
        for row in test_data:
            res = float(row['Result'])
            self.assertEqual(self.calculator.subRes(row['Value 2'], row['Value 1']), res)
            self.assertEqual(self.calculator.res, res)

    def test_results_property(self):
        self.assertEqual(self.calculator.res, 0)


if __name__ == '__main__':
    unittest.main()