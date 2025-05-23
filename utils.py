from typing import TypeVar, Callable, Tuple, Optional, Any, cast, ParamSpec, overload, Union, TypeGuard

# Type variables for generic function
T = TypeVar('T')
P = ParamSpec('P')
E = TypeVar('E', bound=Exception)

def try_except(func: Callable[[], T]) -> Union[
    Tuple[T, None],           # Success case: result is T, error is None
    Tuple[None, Exception]    # Error case: result is None, error is Exception
]:
    """
    Execute a function and catch any exceptions, returning a tuple of (result, error).
    If successful, error will be None and result is guaranteed to be T.
    If an exception occurs, result will be None and error will be the Exception.
    
    Args:
        func: A callable that takes no arguments and returns T
        
    Returns:
        Union[Tuple[T, None], Tuple[None, Exception]]: Either (result, None) or (None, error)
    """
    try:
        result = func()
        return result, None
    except Exception as e:
        return None, e

def is_success(result: Tuple[Optional[T], Optional[Exception]]) -> TypeGuard[Tuple[T, None]]:
    return result[0] is not None and result[1] is None

def is_error(result: Tuple[Optional[Any], Optional[Exception]]) -> TypeGuard[Tuple[None, Exception]]:
    return result[0] is None and result[1] is not None