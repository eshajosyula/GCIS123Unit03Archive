import more_math

def test_facts_6():
    # setup
    x = 6
    expected = 720

    #invoke
    actual = more_math.fact(x)

    #analyze
    assert actual == expected

def test_root_9():
    # setup
    x = 9
    expected = 3.0

    #invoke
    actual = more_math.root(x)

    #analyze
    assert actual == expected

def test_root_9():
    # setup
    x = 9
    expected = 3.0

    #invoke
    actual = more_math.root(x)

    #analyze
    assert actual == expected

def test_trunk_3():
    # setup
    x = 3
    expected = 3.0

    #invoke
    actual = more_math.trunk(x)

    #analyze
    assert actual == expected

