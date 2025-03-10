# Importing the required libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

# Variable declaration
url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
exchange_rates_fp = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
csv_path = './Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_file = "code_log.txt"


# Log Function
def log_progress(message):
    ''' This function logs the mentioned message at a given stage of the 
    code execution to a log file. Function returns nothing.'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

# Extract function
def extract(url, table_attribs):
    '''Extract data from the website and return a DataFrame.'''
    
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    

    tables = data.find_all('tbody')
    if len(tables) < 3:
        raise ValueError("Expected at least 3 <tbody> elements, but found less")

    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col) < 3:
            continue  # Skip rows with missing data
        
        bank_name = col[0].text.strip()  # Bank Name

        # Extract Market Cap safely
        market_cap_str = col[2].get_text(strip=True).replace(",", "")
        #print(f"Extracted Market Cap String: '{market_cap_str}'")  # Debugging print

        if not market_cap_str:  # Handle empty values
            print("Warning: Market Cap column is empty! Skipping row.")
            market_cap = 0.00
            continue

        try:
            market_cap = float(market_cap_str)
        except ValueError as e:
            print(f"Error converting '{market_cap_str}' to float: {e}")
            continue  # Skip invalid data
            

        data_dict = {"Name": bank_name, "MC_USD_Billion": market_cap}
        df1 = pd.DataFrame(data_dict, index=[0])
        df = pd.concat([df, df1], ignore_index=True)
    #print(df)
    return df

# Transform function

def transform(df, exchange_rates_fp):
    
    # Load exchange rates
    exchange_rates_df = pd.read_csv(exchange_rates_fp)
    
    
    # Ensure 'Market Cap' column exists
    if 'MC_USD_Billion' in df.columns:
        # Merge exchange rates into a dictionary (currency -> rate)
        exchange_rates = dict(zip(exchange_rates_df['Currency'], exchange_rates_df['Rate']))

    # Add Market Cap in different currencies
        for currency, rate in exchange_rates.items():
            df[f'MC_{currency}_Billion'] = round(df['MC_USD_Billion'] * rate,2)
    else:
        raise ValueError("Market Cap column not found in the CSV file.")
        
    #print(df)
    return df

#load to csv
def load_to_csv(df, csv_path):
    ''' This function saves the final dataframe as a `CSV` file 
    in the provided path. Function returns nothing.'''

    df.to_csv(csv_path)

#load to DB
def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final dataframe to as a database table
    with the provided name. Function returns nothing.'''

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

# Run query

def run_query(query_statement, sql_connection):
    ''' This function runs the stated query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

# Log progress
log_progress('Preliminaries complete. Initiating ETL process')
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')
df = transform(df,exchange_rates_fp)
log_progress('Data transformation complete. Initiating Loading process')
load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')
sql_connection = sqlite3.connect('Banks.db')
log_progress('SQL Connection initiated.')
load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Executing queries')
query_statement = f"SELECT * FROM Largest_banks"
run_query(query_statement, sql_connection)
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query_statement, sql_connection)
query_statement = f"SELECT Name from Largest_banks LIMIT 5"
run_query(query_statement, sql_connection)
log_progress('Process Complete.')
sql_connection.close()
log_progress('Server Connection Closed')

