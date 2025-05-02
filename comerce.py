#importning necessary tools
import pandas as pd
import os
import sqlite3

#setting up the connection and cursor for SQLite
connection = sqlite3.connect("comerce.db")
curs = connection.cursor()

#reading csv files into dataframes
capstone_df = pd.read_csv("archive (1)/capstone_data_cleaned.csv")
customer_df = pd.read_csv("archive (1)/customers.csv")
order_df = pd.read_csv("archive (1)/orders.csv")
order_item_df = pd.read_csv("archive (1)/order_items.csv")
payments_df= pd.read_csv("archive (1)/payments.csv")
products_df = pd.read_csv("archive (1)/products.csv")

#adding dataframes to SQLite database
capstone_df.to_sql("capstone_data", connection, if_exists = "replace" , index = False)
customer_df.to_sql("customers" , connection , if_exists = "replace" , index = False)
order_df.to_sql("orders" , connection, if_exists = "replace" , index = False)
order_item_df.to_sql("order_items" , connection , if_exists = "replace" , index = False)
payments_df.to_sql("payments" , connection , if_exists = "replace" , index = False)
products_df.to_sql("products" , connection , if_exists = "replace" , index = False)

connection.commit()
print("DataFrames added to SQLite database")



#Joining orders, customers, order items, and products

curs.execute(''' Select * FROM orders
                 JOIN customers on orders.customer_id = customers.customer_id
                 JOIN order_items ON orders.order_id = order_items.order_id
                 JOIN products ON order_items.product_id = products.product_id
             ''')
results1 = curs.fetchall()
columns1 = [description[0] for description in curs.description]
combined_all_df = pd.DataFrame(results1, columns=columns1)
print("\n--- Combined Data (Orders, Customers, Items, Products) ---")
print(combined_all_df.head())




#Joining order items and products

curs.execute(''' SELECT * FROM order_items 
                 JOIN products on order_items.product_id = products.product_id
             ''')
results2 = curs.fetchall()
columns2 = [description[0] for description in curs.description]
order_items_products_df = pd.DataFrame(results2, columns=columns2)
print("\n--- Combined Data (Order Items and Products) ---")
print(order_items_products_df.head())




#Identifying top selling items

curs.execute(''' SELECT  oi.seller_id,
                 SUM(oi.price * oi.order_item_id) AS total_sales
                 FROM order_items oi
                 GROUP BY oi.seller_id
                 ORDER BY total_sales DESC
                 LIMIT 10; -- Get the top 10
             ''')
results3 = curs.fetchall()
columns3 = [description[0] for description in curs.description]
top_sellers_df = pd.DataFrame(results3, columns=columns3)
print("\n--- Top Selling Sellers ---")
print(top_sellers_df)

 
connection.commit()
connection.close()
