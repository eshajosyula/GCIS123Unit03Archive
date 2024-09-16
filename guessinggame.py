import random

def secret_number():

    num = random.randint(1, 100)
    return num

def main():
    print(secret_number())

main()