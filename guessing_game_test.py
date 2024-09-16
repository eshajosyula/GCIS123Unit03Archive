import guessinggame
import random

def guessing_game_test():
    # setup

    random.seed(1)

    result = guessinggame.secret_number()

    assert result == 18

def test_check_guess_too_low():
    secret = 18
    guess = 48

    result = guessinggame.check_guess(secret, guess)

    