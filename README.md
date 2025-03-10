# Banks Project
Identify the top 10 largest banks globally based on market capitalization (in billion USD). Convert these values into GBP, EUR, and INR using the exchange rates provided in a CSV file. Store the transformed data in both CSV format and as a database table for future reference.

## Step by Step approach

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
    
