from typing import TypeVar, Callable 

# Type variables for generic function
T = TypeVar('T')

def try_except(func: Callable[[], T]) -> T | Exception:
    """
    A utility function that attempts to execute a given function and returns its result.
    If an exception occurs, it returns the exception instead.
    This is useful for handling errors in a clean and concise manner.
    Args:
        func (Callable[[], T]): The function to execute.
    Returns:
        T | Exception: The result of the function or the exception raised.
    """
    try:
        result = func()
        return result
    except Exception as e:
        return e
