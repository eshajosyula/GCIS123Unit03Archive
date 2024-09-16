import math

def add(x, y):
    result = x + y
    return str(x) + "+" + str(y) + "=" + str(result)

def subtract(x, y):
    result = x - y
    return str(x) + "-" + str(y) + "=" + str(result)

def multiply(x, y):
    result = x * y
    return str(x) + "*" + str(y) + "=" + str(result)

def divide(x, y):

    if y == 0:
        result = "NaN"
    else:
        result = x / y
    return str(x) + "/" + str(y) + "=" + str(result)

def exponent(x, y):
    result = math.pow(x, y)
    return str(x) + "^" + str(y) + "=" + str(result)

def main():
    print(exponent(5, 2))

main()