import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import threading
from PIL import Image
from genimage import generate_image
from PIL.Image import Image as Img
#from ImageDB import database
from PIL import Image
from genimage import generate_image
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ImageDB.database import insert_generated_image

def open_file_explorer():
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        filename = os.path.basename(file_path)
        filename_label.config(text=filename)
    else:
        messagebox.showwarning("File Selection", "No file selected or invalid file type.")

def insert_image(image_obj, image_name, loading_window):
        
    # Ask the user if they want to save the image in the database
    save_to_db = messagebox.askyesno("Insert Image", "Do you want to save the generated image to the database?")
    
    if save_to_db:
        # Insert the image into the database
        insert_generated_image(image_obj, image_name)
        # Show a success message
        messagebox.showinfo("Image Generated", "The image has been successfully saved to the database.")
    else:
        messagebox.showinfo("Image Not Saved", "The image was not saved to the database.")

    # Close the loading window
    loading_window.destroy()

def start_image_generation():
    # Creating the loading window
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    
    # Centering the loading window on the screen
    center_x = int(screen_width / 2 - 200)
    center_y = int(screen_height / 2 - 100)
    loading_window.geometry(f'400x200+{center_x}+{center_y}')
    
    # Adding a label to the loading window 
    loading_label = tk.Label(loading_window, text="Generating image...", font=("Helvetica", 14))
    loading_label.pack(expand=True)
    
    # Parameters for the generate_image function
    prompt = entry_var.get()
    image = Image.open(file_path)
    show_image = True
    n = len(os.listdir("AiModel/Trials")) + 1
    image_name = f"output-{n}.jpg"
    save_image_path = f"AiModel/Trials/{image_name}"
    strength = 0.8
    num_inf = 100
    guidance = 15

    image = generate_image(
        prompt,
        image,
        show_image,
        save_image_path,
        strength,
        num_inf,
        guidance
    )

    # Insert the image into the database
    insert_image(image, f"output-{n}.jpg", loading_window)

# Create the main window
root = tk.Tk()
root.title("SKAPA")

# Set the window size
window_width = 600 
window_height = 400  

# Get the dimension of the user's screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# Set the position of the window to the center of the user's screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Lock the window size
root.resizable(False, False)

# Create a StringVar to hold the file path
entry_var = tk.StringVar()

# Create a frame to hold all widgets
main_frame = tk.Frame(root)
main_frame.pack(expand=True)

# Create and place the new label above the text field
prompt_label = tk.Label(main_frame, text="Write a prompt for the image background", font=("Helvetica", 14))
prompt_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

# Create and place the text field inside the main frame
entry = tk.Entry(main_frame, textvariable=entry_var, width=40, font=("Helvetica", 14))  # Decreased width
entry.grid(row=1, column=0, columnspan=2, pady=(10, 10), padx=12)

# Create a frame to hold the button and label
frame = tk.Frame(main_frame)
frame.grid(row=2, column=0, columnspan=2, pady=(20, 10))

# Create and place the label inside the frame with increased font size
label = tk.Label(frame, text="Select an image of your item", font=("Helvetica", 14))
label.pack(side=tk.LEFT, padx=10)

# Create and place the button inside the frame with increased font size
button = tk.Button(frame, text="Browse", command=open_file_explorer, font=("Helvetica", 14))
button.pack(side=tk.LEFT)

# Create a label to display the filename
filename_label = tk.Label(main_frame, text="", font=("Helvetica", 14))
filename_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Create a frame for the action button
action_frame = tk.Frame(main_frame)
action_frame.grid(row=4, column=0, columnspan=2, pady=(10, 20)) 

# Create and place the "Generate image" button inside the action frame
generate_button = tk.Button(action_frame, text="Generate image", command=start_image_generation, font=("Helvetica", 14), bg="lightblue")
generate_button.pack()

# Run the application
root.mainloop()
