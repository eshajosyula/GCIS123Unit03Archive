import guessinggame
import random

def guessing_game_test():
    # setup

    random.seed(1)

    result = guessinggame.secret_number()

    assert result == 18