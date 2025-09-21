import pandas as pd
import re
from io import StringIO

print("script running...")

def parse_airline_data(data_string):
    
    rows = data_string.strip().split('\n')
    
    headers = rows[0].split(';')
    print(f"headers: {headers}")
    
    data_rows = []
    for i, row in enumerate(rows[1:], 1):
        if row.strip():
            row_data = row.split(';')
            data_rows.append(row_data)
            print(f"Row {i}: {row_data}")
    
    df = pd.DataFrame(data_rows, columns=headers)
    print(f"\ninitial DataFrame shape: {df.shape}")
    print(df.head())
    
    return df


def main():
   
    data_string = "Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n\"\"\".\.Lufthansa.\.\"\"\";[12, 33];20055.0;london_MONTreal\n"
    
    print("--- AIRLINE DATA TRANSFORMATION ---")
    # print("-"*50)
    
    df = parse_airline_data(data_string)
    
    return df

if __name__ == "__main__":
    result_df = main()