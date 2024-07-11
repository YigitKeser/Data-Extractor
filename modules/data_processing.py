import pandas as pd
from numbers_parser import Document

def extract_data(input_file):
    try:
        doc = Document(input_file)
        sheets = doc.sheets
        tables = sheets[0].tables
        data = tables[0].rows(values_only=True)
        df = pd.DataFrame(data[1:], columns=data[0])
        df.dropna(axis=1, how='all', inplace=True)
        df['credit_date'] = pd.to_datetime(df['credit_date'])
        return df
    except Exception as e:
        print(f"Error extracting data: {e}")
        raise

def save_to_csv(df, output_file):
    try:
        df.to_csv(output_file, index=False)
    except Exception as e:
        print(f"Error saving CSV: {e}")
        raise
