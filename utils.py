from typing import TypeVar, Callable, Tuple, Optional, Any, cast, ParamSpec, overload

# Type variables for generic function
T = TypeVar('T')
P = ParamSpec('P')
E = TypeVar('E', bound=Exception)

def try_except(func: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> Tuple[Optional[T], Optional[Exception]]:
    """
    Execute a function and catch any exceptions, returning a tuple of (result, error).
    If successful, error will be None. If an exception occurs, result will be None.
    
    Args:
        func: The function to execute
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function
        
    Returns:
        Tuple[Optional[T], Optional[Exception]]: A tuple containing (result, error)
    """
    try:
        result = func(*args, **kwargs)
        return result, None
    except Exception as e:
        return None, e
