from typing import TypeVar, Callable, Tuple

# Type variables for generic function
T = TypeVar('T')

def try_except(func: Callable[[], T]) -> Tuple[T, None] | Tuple[None, Exception]:
    try:
        result = func()
        return result, None
    except Exception as e:
        return None, e
