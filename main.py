from calculator import Calculator
calc = Calculator()
while True:
    n = 0
    Exp = input("print expression(format: x+y or x-y or x*y or x:y or x/y)")
    for i in range(1, len(Exp)):
        if Exp[i] == "+" or Exp[i] == "-" or Exp[i] == "*" or Exp[i] == "/" or Exp[i] == ":":
            n = i
            op = Exp[i]
            break
    if n == 0:
        print('No sign of the operation')
        continue
    try:
        a = float(Exp[:n])
        b = float(Exp[n+1:])
    except ValueError:
        print('wrongly entered value')
        continue

    if op == '+':
        ans = calc.add(a, b)
    elif op == '-':
        ans = calc.subtract(a, b)
    elif op == '*':
        ans = calc.multiply(a, b)
    elif op == ':' or op == '/':
        if b == 0:
            print('cant zero division')
            continue
        ans = calc.divide(a, b)
    if op == ':':
        Exp = str(a) + "/" + str(b)
    if ans == calc.evaluate(Exp):
        print(Exp + "=" + str(ans))
    else:
        print('Sorry, we cant find right answer')
