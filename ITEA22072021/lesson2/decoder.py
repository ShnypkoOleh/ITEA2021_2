from typing import Callable
import datetime
import logging

def log(fn: Callable)->Callable:
    def wrapper(*args, **kwargs):
        started_at=datetime.datetime.now()
        logging.error(f"Function {fn.__name__} started at {started_at}.")
        result = fn(*args, **kwargs)
        finished_at =  datetime.datetime.now()
        logging.error(f"Function {fn.__name__} finished at {finished_at}.")
        return result
    return wrapper

def log_whith_exc(fn: Callable)->Callable:
    def wrapper():
        started_at=datetime.datetime.now()
        logging.error(f"Function {fn.__name__} started at {started_at}.")
        try:
            result = fn()
        except Exception as e:
            logging.critical(f"Caugthj error: {e}")
        else :
            finished_at =  datetime.datetime.now()
            logging.error(f"Function {fn.__name__} finished at {finished_at}.")
            return result
    return wrapper



#
# @log_whith_exc
# def show_greeteeng():
#     print("Hello")
#     raise ValueError("haha")

@log
def factorial(number:int)-> int:
    if number ==1:
        return 1
    if number ==0:
        return 1
    return number * factorial(number-1)

print(factorial(15))