from unittest import TestCase
import unittest
from calculator import Calculator


NUM = [6, 3, -8, 4, 4, -3, -7, -8, 2.7, 3.56, -4.44, 6.759, 5.53, -7.68, -24.9, -6.53, 0, -3.43, 0, 0, 4.7, 0]
class CalculatorTest(TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        Answ = [9, -4, 1, -15, 6.26, 2.319, -2.1499999999999995, -31.43, -3.43, 0, 4.7]
        for i in range(0, 11):
            self.assertEqual(Answ[i], self.calc.add(NUM[2*i], NUM[2*i+1]), str(i))

    def test_subtract(self):
        Answ = [3, -12, 7, 1, -0.8599999999999999, -11.199000000000002, 13.21, -18.369999999999997, 3.43, 0, 4.7]
        for i in range(0, 11):
            self.assertEqual(Answ[i], self.calc.subtract(NUM[2*i], NUM[2*i+1]), str(i))

    def test_multiply(self):
        Answ = [18, -32, -12, 56, 9.612, -30.009960000000003, -42.4704, 162.597, -0, 0, 0]
        for i in range(0, 11):
            self.assertEqual(Answ[i], self.calc.multiply(NUM[2*i], NUM[2*i+1]), str(i))

    def test_divide(self):
        Answ = [2, -2, -1.3333333333333333, 0.875, 0.7584269662921349, -0.656901908566356, -0.7200520833333334, 3.813169984686064, -0]
        for i in range(0, 9):
            self.assertEqual(Answ[i], self.calc.divide(NUM[2*i], NUM[2*i+1]), str(i))
        self.assertEqual(ZeroDivisionError, self.calc.divide(4.7, 0))

    def test_evaluate(self):
        self.assertEqual(-6, self.calc.evaluate("3+(4-7)*3"))
        self.assertEqual(17, self.calc.evaluate("2.5*3.2+(4.7-3.2)*6"))
        self.assertEqual(ZeroDivisionError, self.calc.evaluate("2/0"))