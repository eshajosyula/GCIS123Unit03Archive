def convert_height():
    inches = int(input("Enter your height in inches: "))    #enter inches
    #print(inches)              "troubleshooting"
    feet = int(inches/12)   #converts feet
    #print(feet)              "troubleshooting"
    inc = int(inches % 12)  #converts inches
    #print(inc)              "troubleshooting"
    print("You are ", feet, "' ", inc, '"' , " tall", sep = "") #print

def before(letter):
    now = ord(letter)   #gets the ascii value of a character
    prev1 = chr(now - 1)   #gets the ascii value of the previous char and coverts to char
    prev2 = chr(now - 2)   #gets the ascii value of the previous char and coverts to char
    prev3 = chr(now - 3)   #gets the ascii value of the previous char and coverts to char

    print(letter, prev1, prev2, prev3, sep = "\n")  #print
    

def main():
    convert_height()
    before("X")

main()