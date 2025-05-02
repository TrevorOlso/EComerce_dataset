# E-commerce Data Analysis with SQLite

## Overview

This program demonstrates basic data handling and SQL querying on a set of e-commerce data. It reads several CSV files, loads them into separate tables in an SQLite database named `comerce.db`, and then executes a series of SQL queries to explore and combine the data. The results of each query are then displayed using the pandas library.

## Data Source

Due to the large size of the raw data, the CSV files used by this program can be downloaded from the following Google Drive link:

[E-commerce Data Download](https://drive.google.com/drive/folders/15_DS37NN1pt02KFAnkyFMhhdZaf894n_?usp=drive_link)

Please download all the `.csv` files from this link and ensure they are placed in the same directory and in a folder names "Archive (1)" as the Python script before running the program. The expected files are:

* `capstone_data_cleaned.csv`
* `customers.csv`
* `orders.csv`
* `order_items.csv`
* `payments.csv`
* `products.csv`

## Prerequisites

* **Python 3.x** installed on your system.
* **pandas** library: You can install it using pip:
    ```bash
    pip install pandas
    ```
* **sqlite3** library: This is usually included with standard Python installations.

## Setup

1.  **Save the Python script:** Save the provided Python code as a `.py` file (e.g., `commerce.py`) in a directory of your choice.
2.  **Download Data:** Download all the CSV files from the [E-commerce Data Download](https://drive.google.com/drive/folders/15_DS37NN1pt02KFAnkyFMhhdZaf894n_?usp=drive_link) link.
3.  **Place CSV Files:** Ensure all the downloaded `.csv` files are in the **same directory** where you saved the Python script.

## Running the Program

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** where you saved the Python script and the CSV files.
3.  **Run the script** using the Python interpreter:
    ```bash
    python3 commerce.py
    ```

## Output

The program will perform the following actions and print the results to the console:

1.  **Load CSV data into SQLite:** It will create an SQLite database named `comerce.db` (or overwrite it if it already exists) and create tables for each CSV file:
    * `capstone_data`
    * `customers`
    * `orders`
    * `order_items`
    * `payments`
    * `products`
    The program will print a confirmation message once the data is loaded.

2.  **Execute SQL Queries and Display Results:** It will then execute the following SQL queries and display the first few rows of the resulting dataframes using pandas:
    * A query joining the `orders`, `customers`, `order_items`, and `products` tables.
    * A query joining the `order_items` and `products` tables.
    * A query to identify the top 10 sellers based on the total sales.

## Demonstrates Skills

This program demonstrates the following skills:

* **Data Loading:** Reading data from CSV files using pandas.
* **Database Interaction:** Creating and connecting to an SQLite database using the `sqlite3` library.
* **Data Persistence:** Writing pandas DataFrames to an SQLite database as tables.
* **SQL Querying:** Executing `JOIN` clauses to combine data from multiple tables.
* **SQL Ordering and Limiting:** Using `ORDER BY` to sort results and `LIMIT` to retrieve a specific number of rows.
* **Data Display:** Displaying tabular data using pandas DataFrames.

## Further Exploration

This is a basic example. You can extend this program to perform more complex analyses, such as:

* Calculating customer lifetime value.
* Analyzing shipping costs and delivery times.
* Identifying popular product categories in different regions.
* Performing time-series analysis on order data.
* Visualizing the results using libraries like Matplotlib or Seaborn.

You can modify the SQL queries within the Python script to explore different aspects of the e-commerce data. Remember to consult the schema of your database tables to construct effective queries.


Author: TrevorOlso
