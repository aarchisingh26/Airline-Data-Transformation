# Airline-Data-Transformation

This is a Python script that parses messy airline data and cleans it up according to specific instructions.

## Functionality

Takes raw string data, that represents a table, and transforms it transforms it into a clean pandas DataFrame with proper data types and formatting.

## Key Transformations

### 1. FlightCodes Column
- **Problem**: Missing values (empty cells)
- **Solution**: Calculates missing values using +10 increment rule
- **Logic**: Finds first valid FlightCode, calculates base value, generates sequence

### 2. To_From Column  
- **Problem**: Combined origin/destination in single column
- **Solution**: Splits on `_` delimiter into separate `To` and `From` columns
- **Bonus**: Converts to uppercase for consistency

### 3. Airline Code Column
- **Problem**: Inconsistent formatting with punctuation and numbers
- **Solution**: Regex cleaning to extract only airline names
- **Rules**: Remove all punctuation, numbers, and extra whitespace

## Dependencies
```python
import pandas as pd
import re
```

## Usage
```python
python main.py
```

## Functions
- `parse_airline_data()` - Converts string to DataFrame
- `transform_flight_codes()` - Handles missing FlightCodes with interpolation
- `split_to_from_column()` - Separates To_From into two columns  
- `clean_airline_codes()` - Strips punctuation from airline names
- `main()` - Runs the entire pipeline using the other functions