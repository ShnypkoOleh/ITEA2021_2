from typing import Callable

def check_authentication():
    """
    Check if user is authentication in the system(identified)
    """

    if user_is_not_authentication:
        raise AUthenticationError()

def log_operation(fn: Callable) ->  Callable:
    def wrapper():
        #do smth
        result=fn()
        #do smth2
        return result
    return wrapper


@log_operation
def get_accounts_for_client(client_id: int)->list:
    check_authentication()
    """
    get accounts from Database by client_id
    prepare response from accounts
    return response to browser
    """

get_accounts_for_client(...)