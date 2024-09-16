import random

MIN = 1
MAX = 100

num = random.randint(MIN, MAX)

def secret_number():

    #num = random.randint(MIN, MAX)
    return num

def check_guess(secret, guess):
    
    if guess < secret:
        return "too low"
    if guess > secret:
        return "too high"
    else:
        return "correct!"


def main():
    check_guess(18, 48)

main()