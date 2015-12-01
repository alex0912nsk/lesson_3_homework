from unittest import TestCase
from calculator import Calculator
from __init__ import data_provider


class CalculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    operations = lambda: ((6, 3, 9), (-8, 4, -4), (4, -3, 1), (-7, -8, -15), (2.7, 3.56, 6.26), (-4.44, 6.759, 2.319),
                          (5.53, -7.68, -2.15), (-24.9, -6.53, -31.43), (0, -3.43, -3.43), (0, 0, 0), (4.7, 0, 4.7))

    @data_provider(operations)
    def test_add(self, a, b, ans):
        self.assertEqual(ans, round(self.calc.add(a, b), 3))

    operations = lambda: ((6, 3, 3), (-8, 4, -12), (4, -3, 7), (-7, -8, 1), (2.7, 3.56, -0.86), (-4.44, 6.759, -11.199),
                          (5.53, -7.68, 13.21), (-24.9, -6.53, -18.37), (0, -3.43, 3.43), (0, 0, 0), (4.7, 0, 4.7))

    @data_provider(operations)
    def test_subtract(self, a, b, ans):
            self.assertEqual(ans, round(self.calc.subtract(a, b), 3))

    operations = lambda: ((6, 3, 18), (-8, 4, -32), (4, -3, -12), (-7, -8, 56), (2.7, 3.56, 9.612), (-4.44, 6.759, -30.01),
                          (5.53, -7.68, -42.47), (-24.9, -6.53, 162.597), (0, -3.43, -0), (0, 0, 0), (4.7, 0, 0))

    @data_provider(operations)
    def test_multiply(self, a, b, ans):
            self.assertEqual(ans, round(self.calc.multiply(a, b), 3))

    operations = lambda: ((6, 3, 2), (-8, 4, -2), (4, -3, -1.333), (-7, -8, 0.875), (2.7, 3.56, 0.758), (-4.44, 6.759, -0.657),
                          (5.53, -7.68, -0.72), (-24.9, -6.53, 3.813), (0, -3.43, -0))

    @data_provider(operations)
    def test_divide(self, a, b, ans):
        self.assertEqual(ans, round(self.calc.divide(a, b), 3))
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(4.7, 0)

    def test_evaluate(self):
        self.assertEqual(-6, self.calc.evaluate("3+(4-7)*3"))
        self.assertEqual(17, self.calc.evaluate("2.5*3.2+(4.7-3.2)*6"))
        with self.assertRaises(ZeroDivisionError):
            self.calc.evaluate("2/0")
