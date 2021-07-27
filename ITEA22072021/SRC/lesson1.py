#import datetime
#def outside_func():
 #   value=3
 #   def foo():
#        print(value)
 #   foo()

#outside_func()



#def foo():
#   value=2
#    print(value)


#foo()

# def get_current_date()->str:
#     return datetime.datetime.now("%d.%m.%Y")
#
# def print_greeting():
#     name = input("Name:")
#     surname = input("Surname:")
#    # current_date=get_current_date()
#     #output_string= "Hello, "+ name+ " " +surname+ "! It's"+current_date
#     print("Hello, " + name + " " + surname + " ! It's" + get_current_date())
#
# print_greeting()


def factorial(number: int)->int:
    if number ==0:
        return 1
    if number ==1:
        return 1
    return number* factorial(number-1)

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

    value = -5
    try:
        factorial(value)
    except ValueError:
        pass
    else:
        assert False



if __name__=='__name__':
    test_factorial()