import pandas as pd
import re
from datetime import datetime

DATA_STRING = "Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n\"\"\".\.Lufthansa.\.\"\"\";[12, 33];20055.0;london_MONTreal\n"

def parse_airline_data(data_string):
    """
    This function parses a string of airline data and transforms it according to given requirements.
    """
    
    rows = data_string.strip().split('\n')
    
    headers = rows[0].split(';')
    # print(f"headers: {headers}")
    
    data_rows = []
    for i, row in enumerate(rows[1:], 1):
        if row.strip():
            row_data = row.split(';')
            data_rows.append(row_data)
            # print(f"Row {i}: {row_data}")
    
    df = pd.DataFrame(data_rows, columns=headers)
    # print(f"\ninitial DataFrame shape: {df.shape}")
    # print(df.head())
    
    return df

def transform_flight_codes(df):
    """
    This function transforms the FlightCodes column according to requirement 1:
    - fill missing values with incremented values (increment by 10) then convert to int type
    """
   
    df['FlightCodes'] = df['FlightCodes'].replace('', pd.NA)
    df['FlightCodes'] = pd.to_numeric(df['FlightCodes'], errors='coerce')
    
    # print("Original values:")
    # print(df['FlightCodes'].tolist())
    
    
    first_valid_idx = None
    first_valid_value = None
    
    
    for i in range(len(df)):
        if not pd.isna(df.loc[i, 'FlightCodes']):
            first_valid_idx = i
            first_valid_value = df.loc[i, 'FlightCodes']
            break
    
    if first_valid_value is not None:
        base_val = first_valid_value - (first_valid_idx * 10)
        
        
        for i in range(len(df)):
            df.loc[i, 'FlightCodes'] = base_val + (i * 10)
    else:
        base_val = 20000
        for i in range(len(df)):
            df.loc[i, 'FlightCodes'] = base_val + (i * 10)
    
    
    df['FlightCodes'] = df['FlightCodes'].astype(int)
    
    # print("updated FlightCodes values:")
    # print(df['FlightCodes'].tolist())
    
    return df



def split_to_from_column(df):
    """
    This function transforms the To_From column according to requirement 2:
    - split into separate 'To' and 'From' columns then convert to uppercase case
    """
   
    to_from_split = df['To_From'].str.split('_', expand=True)
    
    df['To'] = to_from_split[0].str.upper()
    df['From'] = to_from_split[1].str.upper()
    
    # print("TO column values:")
    # print(df['To'].tolist())
    
    # print("FROM column values:")
    # print(df['From'].tolist())
    
    df = df.drop('To_From', axis=1)
    return df

def clean_airline_codes(df):
    """
    This function cleans the Airline Code column according to requirement 3:
    - remove punctuation except spaces in the middle
    """
    def clean_airline_name(name):
        if pd.isna(name):
            return name
        
        cleaned = re.sub(r'^[^\w\s]+|[^\w\s]+$', '', name)
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
        cleaned = re.sub(r'[0-9]', '', cleaned)        
        cleaned = ' '.join(cleaned.split())
        
        return cleaned
    
    # print("original Airline Code values:")
    
    # print(df['Airline Code'].tolist())
    
    df['Airline Code'] = df['Airline Code'].apply(clean_airline_name)
    
    # print("cleaned-up Airline Code values:")
    # print(df['Airline Code'].tolist())
    
    return df


def main():
    
    """
    This is the main function to execute the complete data transformation pipeline.
    """
        
    df = parse_airline_data(DATA_STRING)
    
    df = transform_flight_codes(df)
    
    df = split_to_from_column(df)
    
    df = clean_airline_codes(df)
    
    print("\n" + "-"*50)
    print("FINAL AIRLINE FLIGHT CODE TABLE:")
    print("-"*50)
    print(df)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filepath = f"output/results_{timestamp}.csv"

    df.to_csv(filepath, index=False)
    print(f"\nSaved formatted table to {filepath}")
    
    return df

if __name__ == "__main__":
    result_df = main()