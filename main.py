import pandas as pd
from utils import try_except

def main() -> None:
    file_path: str = 'data/pokemon.csv'

    df = try_except(lambda: pd.read_csv(file_path))
    
    if isinstance(df, Exception):
        print(f"Error occurred: {df}")
        return
    print(df.head())
    



if __name__ == "__main__":
    main()
