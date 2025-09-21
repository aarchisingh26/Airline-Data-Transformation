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

def transform_flight_codes(df):
   
    
    df['FlightCodes'] = df['FlightCodes'].replace('', pd.NA)
    df['FlightCodes'] = pd.to_numeric(df['FlightCodes'], errors='coerce')
    
    print("Original values:")
    print(df['FlightCodes'].tolist())
    
    
    base_value = 1010
    
    for i in range(len(df)):
        if pd.isna(df.loc[i, 'FlightCodes']):
            df.loc[i, 'FlightCodes'] = base_value + (i * 10)
        elif i == 0: 
            base_value = df.loc[i, 'FlightCodes'] - 10
    
    df['FlightCodes'] = df['FlightCodes'].astype(int)
    
    print("Transformed FlightCodes values:")
    print(df['FlightCodes'].tolist())
    
    return df



def split_to_from_column(df):
   
   
    to_from_split = df['To_From'].str.split('_', expand=True)
    
    df['To'] = to_from_split[0].str.upper()
    df['From'] = to_from_split[1].str.upper()
    
    print("TO column values:")
    print(df['To'].tolist())
    
    print("FROM column values:")
    print(df['From'].tolist())
    
    df = df.drop('To_From', axis=1)
    return df


def main():
   
    data_string = "Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n\"\"\".\.Lufthansa.\.\"\"\";[12, 33];20055.0;london_MONTreal\n"
    
    print("--- AIRLINE DATA TRANSFORMATION ---")
    
    df = parse_airline_data(data_string)
    
    df = transform_flight_codes(df)
    
    df = split_to_from_column(df)
    
    return df

if __name__ == "__main__":
    result_df = main()