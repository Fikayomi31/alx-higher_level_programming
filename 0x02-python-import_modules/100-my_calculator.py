#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    agr = sys.argv[1:]
    if len(agr) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, b, oper = agr
    if oper not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(a)
    b = int(b)
    if oper == '+':
        result = add(a, b)
    elif oper == '-':
        result = sub(a, b)
    elif oper == '*':
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, oper, b, result))
