from Tools.scripts.treesync import raw_input

from calculator import Calculator
calc = Calculator()
while True:
    Exp = raw_input("print expression(format: x+y or x-y or x*y or x:y or x/y)")
    flag = False
    n = Exp.find('+')
    op = '+'
    if n == -1:
        n = Exp.find('*')
        op = '*'
        if n == -1:
            n = Exp.find(':')
            op = ':'
            if n == -1:
                n = Exp.find('/')
                op = '/'
                if n == -1:
                    n = Exp.find('-')
                    op = '-'
                    if n == 0:
                        flag = True
                        n = Exp.find('-', 1, len(Exp))


    if n == -1:
        print('No sign of the operation')
        continue
    try:
        if op != '-':
            A = list(map(float, Exp.split(op)))
        elif n == Exp.rfind('-'):
            if flag == True:
                A = list(map(float, Exp[1:len(Exp)].split(op)))
                A[0] = -A[0]
            else:
                A = list(map(float, Exp.split(op)))
        else:
            if flag == True:
                A = list(map(str, Exp[1:len(Exp)].split(op)))
                A[0] = -float(A[0])
                A[1] = -float(A[2])
            else:
                A = list(map(str, Exp.split(op)))
                A[0] = float(A[0])
                A[1] = -float(A[2])

    except ValueError:
        print('wrongly entered value')
        continue
    if op == '+':
        ans = calc.add(A[0], A[1])
    elif op == '-':
        ans = calc.subtract(A[0], A[1])
    elif op == '*':
        ans = calc.multiply(A[0], A[1])
    elif op == ':' or op == '/':
        if A[1] == 0:
            print('cant zero division')
            continue
        ans = calc.divide(A[0], A[1])
    if op == ':':
        Exp = str(A[0]) + "/" + str(A[1])
    if ans == calc.evaluate(Exp):
        print(Exp + "=" + str(ans))
    else:
        print('Sorry, we cant find right answer')
