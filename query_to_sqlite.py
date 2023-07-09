#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import the necessary libraries:
import sqlite3
import csv


def query_to_sqlite(database_path,csv_file_path,table_name,sql_query):
    
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    
    # Check if the table already exists
    table_exists_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    cursor.execute(table_exists_query)
    table_exists = cursor.fetchone() is not None

    if not table_exists:
        # Open the CSV file
        with open(csv_file_path, 'r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Read the header row from the CSV file
            header = next(csv_reader)

            # Construct the CREATE TABLE statement based on the CSV header
            create_table_query = f"CREATE TABLE {table_name} ({', '.join(header)})"

            # Execute the CREATE TABLE query
            cursor.execute(create_table_query)

            # Skip the header row
            next(csv_reader)

            # Construct the INSERT statement
            insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(header))})"

            # Insert the data row by row
            cursor.executemany(insert_query, csv_reader)

            # Commit the changes
            connection.commit()

    # Get the column names of the table
    column_names_query = f"PRAGMA table_info({table_name})"
    cursor.execute(column_names_query)
    column_names = [row[1] for row in cursor.fetchall()]


    # Execute the SELECT query
    cursor = connection.execute(sql_query)

    # Fetch all the rows from the query result
    rows = cursor.fetchall()
    
    return rows

