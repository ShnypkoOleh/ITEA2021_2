def sum_numbers(a: int, b: int, c: int) ->int:
    """returns summary of input numbers"""
    return a+b+c

def get_average_value(a: float, b: float, c: float, average_value) ->float:
    """return float"""
    avarage_value = (a+b+c) / 3
    return(average_value)

if __name__ =='__main__':


    first = 100
    second = 200
    third = 1000

    result_value = get_average_value(first, second, third)
    print("Result:", result_value)