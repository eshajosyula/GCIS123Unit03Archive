import math

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


def main() :
    #x = int(input("Enter a value for x: "))
    #res1 = squared(x)
    #res2 = cubed(x)
    #print(res1)
    #print(res2)
    #opps()
    even_or_odd(20)
    even_or_odd(21)


main()

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

