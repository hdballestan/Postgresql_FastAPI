import os
import psycopg2
from faker import Faker
from decouple import config
from constants import DATABASE_CONFIG, TABLE_CREATION_QUERY, INSERT_QUERY

fake = Faker()
countries = [fake.country() for _ in range(10)]
data = [(country, year, round(fake.random_number(digits=5, fix_len=True) + fake.random.random(), 2))
        for country in countries for year in range(1980, 2024)]

def create_and_fill_table():
    """
    Create the table and insert the generated data.
    """
    try:
        connection = psycopg2.connect(**DATABASE_CONFIG)
        cursor = connection.cursor()
        
        ################################### Create table ###################################
        cursor.execute(TABLE_CREATION_QUERY)
        
        ################################### Insert data ####################################
        cursor.executemany(INSERT_QUERY, data)
        
        connection.commit()
        cursor.close()
        connection.close()
        print("Table created and data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_and_fill_table()
