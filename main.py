import pandas as pd
from utils import try_except

def main() -> None:
    file_path: str = 'data/pokemon.csv'

    df, err = try_except(lambda: pd.read_csv(file_path))
    
    # exhibit 1
    if err:
        print(f"Error reading the file: {err}")
        return
    # errors when used outside of if block ❌ 
    print(df.head())

    # exhibit 2
    if err:
        print(f"Error reading the file: {err}")
    else:
        # errors when used inside of if block ❌ 
        print(df.head())
    
    # exhibit 3
    if err:
        print(f"Error reading the file: {err}")
    elif df is not None: 
        # does not error when i check if df is not None ✅ 
        # but i do not want to nest it inside, thats similar to try except
        print(df.head())
        
    # exhibit 4
    if err or df is None:
        print(f"Error reading the file: {err}")
    # errors when used outside of if block even after checking for None ❌
    print(df.head())

    # ideal solution
    if err:
        return
    # should not error
    print(df.head())

if __name__ == "__main__":
    main()
