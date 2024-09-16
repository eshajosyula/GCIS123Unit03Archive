import activities

def test_squared_8():
    # setup
    x = 8
    expected = 64

    #invoke
    actual = activities.squared(x)

    #analyze
    assert actual == expected


def test_cubed_2():
    x = 2
    expected = 8

    actual = activities.cubed(x)

    assert actual == expected


def even_or_odd20(x):
    x = 20
    expected = " is positive"

    actual = activities.even_or_odd(x)

    assert actual == expected


def even_or_odd21(x):
    x = 21
    expected = " is odd"

    actual = activities.even_or_odd(x)

    assert actual == expected

##did this last class

def test_hypotenuse_435():
    # setup
    adj = 3
    opp = 4
    expected = 5.0

    #invoke
    actual = activities.hypotenuse(adj, opp)

    #analyze
    assert actual == expected

def test_coin_toss_heads():
    # setup
    expected = "heads"

    #invoke
    actual = activities.coin_toss()

    #analyze
    assert actual == expected



