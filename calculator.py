def add(x, y):
    result = x + y
    return str(x) + "+" + str(y) + "=" + str(result)

def subtract(x, y):
    result = x - y
    return str(x) + "-" + str(y) + "=" + str(result)

def multiply(x, y):
    result = x * y
    return str(x) + "*" + str(y) + "=" + str(result)

def main():
    print(add(5, 7))

main()