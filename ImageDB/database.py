import psycopg2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import os

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
            # Construct the path to 'create_table.sql'
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sql_file_path = os.path.join(current_dir, 'create_table.sql')

            # Check if 'create_table.sql' exists
            if os.path.exists(sql_file_path):
                with open(sql_file_path, 'r') as file:
                    sql_commands = file.read()
                cursor.execute(sql_commands)
                connection.commit()
                print("Executed table creation SQL file.")
            else:
                print(f"Error: SQL file not found at {sql_file_path}")
        else:
            print("Table 'images' already exists.")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while creating table: {error}")
    finally:
        if connection:
            connection.close()

def insert_generated_image(image_obj, image_name):
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='imagedb',
            user='postgres',
            password='postgres'
        )
        cursor = connection.cursor()

        # Convert the PIL image object to bytes
        image_bytes = io.BytesIO()
        image_obj.save(image_bytes, format='PNG')  # Save as PNG
        image_bytes = image_bytes.getvalue()  # Get the byte data

        cursor.execute(
            "INSERT INTO images (image_name, image_data) VALUES (%s, %s)",
            (image_name, psycopg2.Binary(image_bytes))
        )
        connection.commit()
        print(f"Inserted generated image '{image_name}' into the database.")
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while inserting generated image: {error}")
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

def display_image_from_database(image_name):
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='imagedb',
            user='postgres',
            password='postgres'
        )
        cursor = connection.cursor()

        # Retrieve image data by name
        cursor.execute("SELECT image_data FROM images WHERE image_name = %s", (image_name,))
        image_data = cursor.fetchone()

        if image_data:
            image_bytes = image_data[0]
            image = Image.open(io.BytesIO(image_bytes))
            image.show()  # This will open the image in the default image viewer
        else:
            print(f"No image found with the name '{image_name}'.")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while retrieving image: {error}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()  # Step 1: Create the database
    create_table()     # Step 2: Create the table in the 'ImageDB' database
    choose_file_and_insert()  # Step 3: Choose a PNG file and insert it into the database
    
    # Example of how to retrieve and display an image from the database:
    # display_image_from_database('your_image_name.png')
