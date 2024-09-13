import activities

def test_squared_8():
    # setup
    x = 8
    expected = 64

    #invoke
    actual = activities.squared(x)

    #analyze
    assert actual == expected
