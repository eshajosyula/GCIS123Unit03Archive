import math

def add(x, y):
    result = x + y
    return str(x) + " + " + str(y) + " = " + str(result)

def subtract(x, y):
    result = x - y
    return str(x) + " - " + str(y) + " = " + str(result)

def multiply(x, y):
    result = x * y
    return str(x) + " * " + str(y) + " = " + str(result)

def divide(x, y):

    if y == 0:
        result = "NaN"
    else:
        result = x / y
    return str(x) + " / " + str(y) + " = " + str(result)

def exponent(x, y):
    result = math.pow(x, y)
    return str(x) + " ^ " + str(y) + " = " + str(result)

def main():
    # user inputs
    x = int(input("enter x: "))
    y = int(input("enter y: "))

    print(
    add(x, y), "\n",
    subtract(x, y), "\n",
    multiply(x, y), "\n",
    divide(x, y), "\n",
    exponent(x, y),
    sep = ""
    )

main()