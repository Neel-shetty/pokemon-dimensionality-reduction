import pandas as pd
from typing import NoReturn, Optional
from utils import try_except

def main() -> None:
    file_path: str = 'data/pokemon.csv'

    df, error = try_except(pd.read_csv, file_path)
    
    if error or df is None:
        return print(f"An error occurred: {error}")
    
    print(f"Head of {file_path}:")
    print(df.head())


if __name__ == "__main__":
    main()
