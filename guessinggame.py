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
    secret = secret_number()
    player_guess = int(input("enter a number: "))
    result = check_guess(secret, player_guess)

    print(result)

if __name__ == "__main__":
    main()