# E-commerce Data Analysis with SQLite

## Overview

This program demonstrates basic data handling and SQL querying on a set of e-commerce data stored in CSV files. It reads several CSV files, loads them into separate tables in an SQLite database named `comerce.db`, and then executes a series of SQL queries to explore and combine the data. The results of each query are then displayed using the pandas library.

## Files

The program expects the following CSV files from the Archive (1) folder to be present in the same directory as the Python script:

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

1.  **Save the Python script:** Save the provided Python code as a `.py` file (e.g., `commerce.py`) in the same directory where your CSV data files are located.
2.  **Ensure CSV files are present:** Make sure all the required CSV files listed above are in the same directory as the Python script.

## Running the Program

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory** where you saved the Python script.
3.  **Run the script** using the Python interpreter:
    ```bash
    python ecommerce_analysis.py
    ```

## Output

The program will perform the following actions and print the results to the console:

1.  **Load CSV data into SQLite:** It will create an SQLite database named `books.db` (or overwrite it if it already exists) and create tables for each CSV file:
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
* **SQL Aggregation:** Using `SUM()` and `GROUP BY` to calculate total sales per seller.
* **SQL Ordering and Limiting:** Using `ORDER BY` to sort results and `LIMIT` to retrieve a specific number of rows.
* **Data Display:** Displaying tabular data using pandas DataFrames.
* **Error Handling:** Basic `try-except` blocks are used to catch potential SQLite errors during query execution.

## Further Exploration

This is a basic example. You can extend this program to perform more complex analyses, such as:

* Calculating customer lifetime value.
* Analyzing shipping costs and delivery times.
* Identifying popular product categories in different regions.
* Performing time-series analysis on order data.
* Visualizing the results using libraries like Matplotlib or Seaborn.

You can modify the SQL queries within the Python script to explore different aspects of the e-commerce data. Remember to consult the schema of your database tables to construct effective queries.


Author: TrevorOlso
