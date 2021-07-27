from typing import Callable
import logging

def congrats(func: Callable)->Callable:
    """

    :type func: object
    """
    def wrapper(*args,**kwargs):

      #  ress= logging.info(f"Well done, your result is {func.__name__}.")
        res = (logging.error(f"Well done, your result is {func(*args, **kwargs)}."))

        return res
    return wrapper

@congrats
def factorial(number:int)-> int:
    if number ==1:
        return 1
    if number ==0:
        return 1
    return number * factorial(number-1)

print(factorial(15))