import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image
from genimage import generate_image
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ImageDB.database import insert_generated_image

def open_file_explorer(file_path_var, filename_label):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        file_path_var.set(file_path)
        filename = os.path.basename(file_path)
        filename_label.config(text="Selected file: " + filename)
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
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    loading_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Adding a label to the loading window 
    loading_label = tk.Label(loading_window, text="Generating image...", font=("Helvetica", 14))
    loading_label.pack(expand=True)
    
    # Parameters for the generate_image function
    prompt = entry_var.get()
    image = Image.open(file_path_var1.get())
    show_image = True
    n = len(os.listdir("ImageGenInterface/Trials")) + 1
    image_name = f"output-{n}.jpg"
    save_image_path = f"ImageGenInterface/Trials/{image_name}"
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
window_width = 1000 
window_height = 800  

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

# Create a StringVar to hold the file paths
file_path_var1 = tk.StringVar()
file_path_var2 = tk.StringVar()

# Create a StringVar to hold the prompt
entry_var = tk.StringVar()

# Create a frame to hold all widgets
main_frame = tk.Frame(root)
main_frame.pack(expand=True)

# Create and place the new label above the text field
prompt_label = tk.Label(main_frame, text="Write a prompt for the image background", font=("Helvetica", 20))
prompt_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

# Create and place the text field inside the main frame
entry = tk.Entry(main_frame, textvariable=entry_var, width=40, font=("Helvetica", 20))  # Decreased width
entry.grid(row=1, column=0, columnspan=2, pady=(10, 10), padx=12)

# Create a frame to hold the button and label
frame = tk.Frame(main_frame)
frame.grid(row=2, column=0, columnspan=2, pady=(20, 10))

# Create and place the label inside the frame with increased font size
label = tk.Label(frame, text="Select an image of your item", font=("Helvetica", 20))
label.pack(side=tk.LEFT, padx=10)

# Create and place the button inside the frame with increased font size
button = tk.Button(frame, text="Browse", command=lambda: open_file_explorer(file_path_var1, filename_label1), font=("Helvetica", 20))
button.pack(side=tk.LEFT)

# Create a label to display the filename to the right of the button
filename_label1 = tk.Label(frame, text="", font=("Helvetica", 15))
filename_label1.pack(side=tk.LEFT, padx=10)

# Create a new frame to hold the new label and button
new_frame = tk.Frame(main_frame)
new_frame.grid(row=5, column=0, columnspan=2, pady=(20, 10))

# Create and place the new label inside the new frame
new_label = tk.Label(new_frame, text="Select another image", font=("Helvetica", 20))
new_label.pack(side=tk.LEFT, padx=10)

# Create and place the new button inside the new frame
new_button = tk.Button(new_frame, text="Browse", command=lambda: open_file_explorer(file_path_var2, filename_label2), font=("Helvetica", 20))
new_button.pack(side=tk.LEFT)

# Create a label to display the filename to the right of the button
filename_label2 = tk.Label(new_frame, text="", font=("Helvetica", 15))
filename_label2.pack(side=tk.LEFT, padx=10)

# Create a frame for the input field
input_frame = tk.Frame(main_frame)
input_frame.grid(row=6, column=0, columnspan=2, pady=(10, 20))

# Define the slider parameters with default values
slider_params = [
    ("Strength", 0, 1, 0.01, 0.8),  # Default value for Strength is 0.8
    ("Guidance", 0, 20, 0.1, 7.5),   # Default value for Guidance is 7.5
    ("Inference", 0, 500, 1, 50)   # Default value for Inference is 50
]

# Create and place the input fields inside the input frame
for i, (label_text, from_, to, resolution, default) in enumerate(slider_params):
    # Create and place the label
    label = tk.Label(input_frame, text=label_text, font=("Helvetica", 14))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    # Create and place the slider with increased width and set default value
    slider = tk.Scale(input_frame, from_=from_, to=to, resolution=resolution, orient=tk.HORIZONTAL, font=("Helvetica", 14), length=350)
    slider.set(default)  # Set the default value
    slider.grid(row=i, column=1, padx=10, pady=5, sticky="e")

    # Create and place the input field next to the slider
    input_field = tk.Entry(input_frame, width=5, font=("Helvetica", 14))
    input_field.insert(0, str(default))  # Set the default value in the input field
    input_field.grid(row=i, column=2, padx=10, pady=5, sticky="e")

    # Function to update slider value when input field changes
    def update_slider(event, slider=slider, input_field=input_field):
        try:
            value = float(input_field.get())
            if from_ <= value <= to:
                slider.set(value)
            else:
                input_field.delete(0, tk.END)
                input_field.insert(0, str(slider.get()))
        except ValueError:
            input_field.delete(0, tk.END)
            input_field.insert(0, str(slider.get()))

    # Function to update input field value when slider changes
    def update_input_field(value, input_field=input_field):
        input_field.delete(0, tk.END)
        input_field.insert(0, str(value))

    # Bind the input field to the update function
    input_field.bind("<Return>", update_slider)
    # Bind the slider to the update function
    slider.config(command=update_input_field)

label = tk.Label(input_frame, text="Negative Prompts", font=("Helvetica", 14))
label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

negative_prompts = tk.Entry(input_frame, width=40, font=("Helvetica", 14))
negative_prompts.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="e")

# Create a frame for the checkboxes
checkbox_frame = tk.Frame(input_frame)
checkbox_frame.grid(row=4, column=0, columnspan=3, pady=(10, 20))

# Create a StringVar to hold the selected mode
mode_var = tk.StringVar(value="performance")

# Create and place the label above the checkboxes
mode_label = tk.Label(checkbox_frame, text="Select Mode", font=("Helvetica", 14))
mode_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Create and place the "Performance mode" checkbox
performance_checkbox = tk.Radiobutton(
    checkbox_frame, text="Performance mode", variable=mode_var, value="performance", font=("Helvetica", 14)
)
performance_checkbox.grid(row=1, column=0, padx=10, pady=5)

# Create and place the "Vanilla mode" checkbox
vanilla_checkbox = tk.Radiobutton(
    checkbox_frame, text="Vanilla mode", variable=mode_var, value="vanilla", font=("Helvetica", 14)
)
vanilla_checkbox.grid(row=1, column=1, padx=10, pady=5)

# Create a frame for the action button
action_frame = tk.Frame(main_frame)
action_frame.grid(row=7, column=0, columnspan=2, pady=(10, 20)) 

# Create and place the "Generate image" button inside the action frame
generate_button = tk.Button(action_frame, text="Generate image", command=start_image_generation, font=("Helvetica", 20), bg="lightblue")
generate_button.pack()

# Run the application
root.mainloop()
