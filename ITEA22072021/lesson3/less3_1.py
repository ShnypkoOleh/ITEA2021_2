import json


def factorial(number) -> int:
    if number == 1:
        return 1
    if number == 0:
        return 1
    return number * factorial(number - 1)



def factorial_json(first: int, last: int):
    liss = []
    for number in range(first, last):
        new_factorial = factorial(number)


        liss.append(f'{str(number)}'+":"+ f'{str(new_factorial)}')

        number = number + 1
        print(liss)

    return json.dumps(liss, indent=4)


print(factorial_json(1, 20))
