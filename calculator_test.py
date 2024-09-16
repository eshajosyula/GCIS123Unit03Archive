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