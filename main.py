import pandas as pd
from utils import is_success, is_error, try_except

# def try_except(t: func, ex: Exception = None):
#   try:
#     result = t()
#     return result
#   except Exception as e:
#     if isinstance(e,ex):
#       return e
#     elif ex is None:
#       return None
#     # else:
#     #   return False


def main() -> None:
    file_path: str = 'data/pokemon.csv'

    res = try_except(lambda: pd.read_csv(file_path))
    
    if is_error(res):
        return
    # if is_success(res):
    data = res[0]
    if data is None:
        return
    data.head()
    



if __name__ == "__main__":
    main()
