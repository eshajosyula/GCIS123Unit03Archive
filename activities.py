## imports
import math
import random

def squared(x) : 
    return math.pow(x, 2)

def cubed(x) :
    return math.pow(x, 3)

#   the result is a float now, not int

def hypotenuse(adj, opp):
    a = math.pow(adj, 2)
    b = math.pow(opp, 2)

    return math.sqrt(a + b)

def opps():
    a = 5
    b = 10
    c = "abc"
    d = "bcd"

    print( a == b )
    print( a != b )
    print( a == (b - 5) )
    print( c == d )
    print( a == c )
    print( a < b )
    print( a <= b )
    print( a > 5 )
    print( a >= 5 )
    print( c > d )
    print( c <= d )
    print( b < c )

def even_or_odd(n):
    if n % 2 == 0:
        print(n, " is positive", sep="")
    else:
        print(n, " is odd", sep="")


"""
Logical Operators

1. F
2. T
3. T
4. T
5. F
6. F
7. T
8. F
9. T
10. F

Relational Operators

1. F
2. T
3. T
4. F
5. F
6. T 
7. T
8. F
9. T
10. F
11. T
12. Error

"""

#   =====================================

def coin_toss():

    random.seed(1)

    x = random.randint(1, 2)

    if x == 1:
        return "heads"
    else:
        return "tails"
    
PI = 3.14159

def circum(r):
    circ = 2 * PI * r
    return circ

def areacirc(r):
    area = PI * r ** 2
    return area
    

def main() :
    #x = int(input("Enter a value for x: "))
    #res1 = squared(x)
    #res2 = cubed(x)
    #print(res1)
    #print(res2)
    #opps()
    #even_or_odd(20)
    #even_or_odd(21)

    """print("1: ", coin_toss(), "\n",
          "2: ", coin_toss(), "\n",
          "3: ", coin_toss(), "\n",
          "4: ", coin_toss(), "\n",
          "5: ", coin_toss(), "\n",
          sep="")
    

    random.seed(1)
    x = random.randint(1, 100)
    y = random.randrange(1, 100)
    z = random.random()

    print(x, y, z)
    """
    circ = circum(2)
    area = areacirc(4)
    print(circ)
    print(area)





if __name__ == "__main__":
    main()

"""The most common errors that I've ran into were regarding typecasting - 
a certain function takes an int vs a float, or vice versa, or a float can't be converted into an int. 
These are an easy fix because I would just need to change the type of variable that I am implementing.
Syntax errors are also pretty common because I am used to Java and might use %% instead of % or forget to use : 
in a conditional and might use {} instead."""