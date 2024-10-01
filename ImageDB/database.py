import psycopg2
import tkinter as tk
from tkinter import filedialog

def create_database():
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',  
            password='postgres' 
        )
        connection.autocommit = True
        cursor = connection.cursor()
        
        try:
            cursor.execute("CREATE DATABASE ImageDB;")
            print("Database 'ImageDB' created successfully.")
        except psycopg2.errors.DuplicateDatabase:
            print("Database 'ImageDB' already exists.")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while creating database: {error}")
    finally:
        if connection:
            connection.close()

def create_table():
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='imagedb',
            user='postgres',
            password='postgres'
        )
        cursor = connection.cursor()
        
        # Check if the table already exists
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name='images'
            );
        """)
        table_exists = cursor.fetchone()[0]
        
        if not table_exists:
            # If the table does not exist, create it
            with open('create_table.sql', 'r') as file:
                sql_commands = file.read()
            cursor.execute(sql_commands)
            connection.commit()
            print("Executed table creation SQL file.")
        else:
            print("Table 'images' already exists.")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while creating table: {error}")
    finally:
        if connection:
            connection.close()

def insert_image(image_path):
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='imagedb',
            user='postgres', 
            password='postgres' 
        )
        cursor = connection.cursor()
        with open(image_path, 'rb') as file:
            image_data = file.read()
            image_name = image_path.split('/')[-1]  # Get the file name
            cursor.execute(
                "INSERT INTO images (image_name, image_data) VALUES (%s, %s)",
                (image_name, psycopg2.Binary(image_data))
            )
            connection.commit()
            print(f"Inserted image '{image_name}' into the database.")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while inserting image: {error}")
    finally:
        if connection:
            connection.close()

def choose_file_and_insert():
    # Open a file dialog to choose a PNG file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a PNG Image",
        filetypes=[("PNG Files", "*.png")]
    )
    
    if file_path:  # If a file was selected
        insert_image(file_path)

if __name__ == "__main__":
    create_database()  # Step 1: Create the database
    create_table()     # Step 2: Create the table in the 'ImageDB' database
    choose_file_and_insert()  # Step 3: Choose a PNG file and insert it into the database
