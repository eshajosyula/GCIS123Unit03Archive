import math

def fact(num):
    if num > 0:
        return math.factorial(num)
    else:
        return 0
    
def root(num):
    if num > 0:
        return float(math.sqrt(num))
    else: 
        return 0
    
def trunk(num):
    return float(math.trunc(num))

def main():
    x = int(input("input a number: "))
    print(fact(x), "\n", root(x), "\n", trunk(x), sep = "")
    #print(trunk(x))

if __name__ == "__main__":
    main()