def convert_height():
    inches = int(input("Enter your height in inches: "))
    #print(inches)              "troubleshooting"
    feet = int(inches/12)
    #print(feet)              "troubleshooting"
    inc = int(inches % 12)
    #print(inc)              "troubleshooting"
    print("You are ", feet, "' ", inc, "''" , " tall", sep = "")

def before(letter):
    now = ord(letter)
    prev1 = chr(now - 1)
    prev2 = chr(now - 2)
    prev3 = chr(now - 3)

    print(letter, prev1, prev2, prev3, sep = "\n")
    

def main():
    convert_height()
    before("X")

main()