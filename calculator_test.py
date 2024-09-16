import calculator

def test_add_57():
    # setup
    x = 5
    y = 7
    expected = "5+7=12"

    #invoke
    actual = calculator.add(x, y)

    #analyze
    assert actual == expected

def test_subtract_217():
    # setup
    x = 2
    y = 17
    expected = "2-17=-15"

    # invoke
    actual = calculator.subtract(x, y)

    # analyze
    assert actual == expected