# Largest Banks Market Capitalization Analysis

## Project Overview

As a data engineer for a research organization, your task is to create an automated system to compile and transform data for the top 10 largest banks globally ranked by market capitalization (in billion USD). The data must be converted into GBP, EUR, and INR using exchange rate information from a CSV file. The processed data will be stored both locally in a CSV file and in a database table for future reference. The system is designed for execution every financial quarter to generate reports.

## Project Structure
```
📁 banks_project
│── banks_project.py          # Main Python script
│── exchange_rate.csv         # Exchange rate dataset (downloaded)
│── Largest_banks_data.csv    # Processed output file
│── Banks.db                  # SQLite database file
│── code_log.txt              # Log file
│── README.md                 # Documentation

```
## Setup Instructions
### Prerequisites
    • Python 3.x
    • Libraries: pandas, requests, BeautifulSoup4, sqlite3
### Running the Project
    1.Extract bank data
    2.Transform the extracted data
    3.Store the transformed data in CSV format
    4.Load data into the database
    5.Run queries on the database
    6.Check the log file for progress tracking


## Task Breakdown:
### 1. Implementing logging function- 
    • Ensure each log entry records timestamps and descriptions of the process.

### 2. Extract Bank Data from the Web -
    • Inspect the webpage structure and identify the table under the section "By market capitalization".
    • Write a function to fetch this tabular data and store it in a dataframe.
    • Call function to verify if the data has been extracted correctly.

### 3. Transform the Dataframe -
    • Load the exchange rates from the provided CSV file.
    • Convert the Market Capitalization (USD) into GBP, EUR, and INR, rounding values to two decimal places.
    • Write a function to perform this transformation.
    • Call the function and verify the updated dataframe.

### 4. Save Data to a CSV File
    • Write a function to export the transformed dataframe into a CSV file.
    • Call the function and confirm the file is saved correctly.

### 5. Load Data into an SQL Database
    • Establish a connection to an SQL database.
    • Write a function to store the dataframe as a table in the database.
    • Call the function and verify the data is successfully stored.

### 6.  Run Queries on the Database
    • Write and execute SQL queries to analyze the stored data.
    • Retrieve specific insights such as the largest bank by market capitalization.

## Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
