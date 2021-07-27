def is_primary(a: int) -> bool:
    b = 2
    if a == 1:
        return b == a
    else:
        while a % b != 0:
            b += 1
        return b == a


# print(is_primary(0))

def test_primary():

    a: int = 145
    expected_primary: bool = False
    result = is_primary(a)
    assert result == expected_primary

    a = 149
    expected_primary = True
    result = is_primary(a)
    assert result == expected_primary

    a = 0
    expected_primary = False
    result = is_primary(a)
    assert result == expected_primary


    try:
        is_primary(a)
    except ValueError:
        False
    else:
        assert True


    a = -144
    expected_primary = False
    result = is_primary(a)
    assert result == expected_primary

    try:
        is_primary(a)
    except ValueError:
        False
    else:
        assert True

# print(is_primary(2))
if __name__ =='__main__':
    test_primary()
