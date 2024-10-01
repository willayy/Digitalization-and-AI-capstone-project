import psycopg2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

def fetch_images():
    connection = None
    images = []
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='imagedb',
            user='postgres',  
            password='postgres' 
        )
        cursor = connection.cursor()
        cursor.execute("SELECT image_name, image_data FROM images;")
        rows = cursor.fetchall()
        
        for row in rows:
            image_name = row[0]
            image_data = row[1]
            images.append((image_name, image_data))
        
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while fetching images: {error}")
    finally:
        if connection:
            connection.close()
    return images

def show_images():
    images = fetch_images()
    
    if not images:
        messagebox.showinfo("No Images", "No images found in the database.")
        return

    root = tk.Tk()
    root.title("Images from Database")

    for index, (image_name, image_data) in enumerate(images):
        # Convert binary data to an image
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail((200, 200))  # Resize the image
        img = ImageTk.PhotoImage(image)

        # Create a label to display the image
        label = tk.Label(root, image=img)
        label.image = img  # Keep a reference to avoid garbage collection
        label.grid(row=index // 3, column=index % 3)  # Arrange in a grid

        # Create a label for the image name
        name_label = tk.Label(root, text=image_name)
        name_label.grid(row=index // 3 + 1, column=index % 3)

    root.mainloop()

if __name__ == "__main__":
    show_images()  # Show images from the database
