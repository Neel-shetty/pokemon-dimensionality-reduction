import pandas as pd
from typing import NoReturn, Optional

def main() -> None:
    try:
        file_path: str = 'data/pokemon.csv'
        df: pd.DataFrame = pd.read_csv(file_path)
        print(f"Head of {file_path}:")
        print(df.head())
    except FileNotFoundError:
        print(f"Error: File not found. Please ensure 'data.csv' exists in the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
