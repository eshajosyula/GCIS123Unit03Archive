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
