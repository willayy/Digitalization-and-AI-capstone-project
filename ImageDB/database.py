import psycopg2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io
import os
import sys

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
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sql_file_path = os.path.join(current_dir, 'create_table.sql')

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
        image_obj.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()

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

def insert_image(file_path):
    image_obj = Image.open(file_path)
    image_name = os.path.basename(file_path)
    insert_generated_image(image_obj, image_name)

def choose_file_and_insert():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PNG Image",
        filetypes=[("PNG Files", "*.png")]
    )

    if file_path:
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

        cursor.execute("SELECT image_data FROM images WHERE image_name = %s", (image_name,))
        image_data = cursor.fetchone()

        if image_data:
            image_bytes = image_data[0]
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
        else:
            print(f"No image found with the name '{image_name}'.")

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while retrieving image: {error}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <command> [arguments]")
        print("Commands:")
        print("  create_database          - Create the ImageDB database")
        print("  create_table             - Create the 'images' table")
        print("  insert_image <filepath>  - Insert a PNG image from the specified file path")
        print("  display_image <name>     - Display an image from the database by its name")
    else:
        command = sys.argv[1]

        if command == "create_database":
            create_database()

        elif command == "create_table":
            create_table()

        elif command == "insert_image":
            if len(sys.argv) < 3:
                print("Usage: insert_image <filepath>")
            else:
                file_path = sys.argv[2]
                if os.path.exists(file_path):
                    insert_image(file_path)
                else:
                    print(f"Error: File not found at {file_path}")

        elif command == "display_image":
            if len(sys.argv) < 3:
                print("Usage: display_image <name>")
            else:
                image_name = sys.argv[2]
                display_image_from_database(image_name)

        else:
            print(f"Unknown command: {command}")
