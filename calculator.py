class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""

        try:
            float(x)
            float(y)
            return x+y
        except ValueError:
            return None

    def subtract(self, x, y):
        """This function subtracts two numbers"""

        try:
            float(x)
            float(y)
            return x-y
        except ValueError:
            return None

    def multiply(self, x, y):
        """This function multiplies two numbers"""

        try:
            float(x)
            float(y)
            return x*y
        except ValueError:
            return None

    def divide(self, x, y):
        """This function divides two numbers"""

        try:
            float(x)
            float(y)
            if y == 0:
                raise ZeroDivisionError('Нельзя делить на 0')
            return x/y
        except ValueError:
            return None

    def evaluate(self, expression):
        """This function evaluate expression"""

        return eval(expression)

