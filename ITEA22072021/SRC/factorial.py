

def factorial(number)->int:
    if number ==1:
        return 1
    if number ==0:
        return 1
    return number * factorial(number-1)

def test_factorial():
    """
    --number <0
    --type of number
    +correct value(positive test)
    -- to large number
    +number=0

    """
    value: int = 6
    expected_factorial: int = 720
    result = factorial(value)
    assert result == expected_factorial

    value =0
    expected_factorial=1
    result = factorial(value)
    assert result == expected_factorial
    print(factorial(value))

    try:
        factorial(value)
    except ValueError:
        pass
    else:
        assert False




if __name__=='__name__':
    test_factorial()