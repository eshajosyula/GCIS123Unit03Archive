import calculator

def test_add_57():
    # setup
    x = 5
    y = 7
    expected = "5 + 7 = 12"

    #invoke
    actual = calculator.add(x, y)

    #analyze
    assert actual == expected

def test_subtract_217():
    # setup
    x = 2
    y = 17
    expected = "2 - 17 = -15"

    # invoke
    actual = calculator.subtract(x, y)

    # analyze
    assert actual == expected

def test_multiply_39():
    # setup
    x = 3
    y = 9
    expected = "3 * 9 = 27"

    # invoke
    actual = calculator.multiply(x, y)

    # analyze
    assert actual == expected

def test_divide_NaN():
    # setup
    x = 3
    y = 0
    expected = "3 / 0 = NaN"

    # invoke
    actual = calculator.divide(x, y)

    # analyze
    assert actual == expected

def test_divide_126():
    # setup
    x = 12
    y = 6
    expected = "12 / 6 = 2.0"

    # invoke
    actual = calculator.divide(x, y)

    # analyze
    assert actual == expected

def test_divide_52():
    # setup
    x = 5
    y = 2
    expected = "5 ^ 2 = 25.0"

    # invoke
    actual = calculator.exponent(x, y)

    # analyze
    assert actual == expected
