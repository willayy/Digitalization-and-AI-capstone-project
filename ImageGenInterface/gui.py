import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image
import sys
import subprocess
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
        
def start_image_generation(prompt, object_path, mask_path, strength, guidance, inference, negative_prompt, mode):
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
    image = Image.open(object_path)
    show_image = True
    n = len(os.listdir("ImageGenInterface/Trials")) + 1
    image_name = f"output-{n}.jpg"
    save_image_path = f"ImageGenInterface/Trials/{image_name}"

    image = generate_image(
        prompt,
        image,
        show_image,
        save_image_path,
        strength,
        inference,
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
object_file_path = tk.StringVar()
mask_file_path = tk.StringVar()

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
def create_file_selector(frame, label_text, file_path_var, row):
    file_frame = tk.Frame(frame)
    file_frame.grid(row=row, column=0, columnspan=2, pady=(20, 10))

    # Create and place the label inside the frame with increased font size
    file_label = tk.Label(file_frame, text=label_text, font=("Helvetica", 20))
    file_label.pack(side=tk.LEFT, padx=10)

    # Create and place the button inside the frame with increased font size
    file_button = tk.Button(file_frame, text="Browse", command=lambda: open_file_explorer(file_path_var, filename_label), font=("Helvetica", 20))
    file_button.pack(side=tk.LEFT)

    # Create a label to display the filename to the right of the button
    filename_label = tk.Label(file_frame, text="", font=("Helvetica", 15))
    filename_label.pack(side=tk.LEFT, padx=10)

# Create and place the file selectors
create_file_selector(main_frame, "Select object image", object_file_path, 2)
create_file_selector(main_frame, "Select object image mask", mask_file_path, 5)

# Create a frame for the input field
input_frame = tk.Frame(main_frame)
input_frame.grid(row=6, column=0, columnspan=2, pady=(10, 20))

# Define the slider parameters with default values
slider_params = [
    ("Strength", 0, 1, 0.01, 0.8),   # Default value for Strength is 0.8
    ("Guidance", 0, 20, 0.1, 7.5),   # Default value for Guidance is 7.5
    ("Inference", 0, 500, 1, 50)     # Default value for Inference is 50
]

# Create and place the input fields inside the input frame
for i, (label_text, from_, to, resolution, default) in enumerate(slider_params):
    # Create and place the label
    label = tk.Label(input_frame, text=label_text, font=("Helvetica", 14))
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    # Create and place the slider with increased width and set the default value
    slider = tk.Scale(input_frame, from_=from_, to=to, resolution=resolution, orient=tk.HORIZONTAL, font=("Helvetica", 14), length=350)
    slider.set(default)  # Set the default value
    slider.grid(row=i, column=1, padx=10, pady=5, sticky="e")

    # Assign each slider to a specific variable for later access
    if label_text == "Strength":
        strength_slider = slider
    elif label_text == "Guidance":
        guidance_slider = slider
    elif label_text == "Inference":
        inference_slider = slider

    # Create and place the input field next to the slider
    input_field = tk.Entry(input_frame, width=5, font=("Helvetica", 14))
    input_field.insert(0, str(default))  # Set the default value in the input field
    input_field.grid(row=i, column=2, padx=10, pady=5, sticky="e")

    # Function to update the slider value when the input field changes
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

    # Function to update the input field value when the slider changes
    def update_input_field(value, input_field=input_field):
        input_field.delete(0, tk.END)
        input_field.insert(0, str(value))

    # Bind the input field to the update function
    input_field.bind("<Return>", update_slider)
    # Bind the slider to the update function
    slider.config(command=update_input_field)


negative_prompt_label = tk.Label(input_frame, text="Negative Prompts", font=("Helvetica", 14))
negative_prompt_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

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

def on_generate_button_click():
    # Get values from the UI elements
    prompt = entry_var.get()
    object_path = object_file_path.get()
    mask_path = mask_file_path.get()
    strength = strength_slider.get()
    guidance = guidance_slider.get()
    inference = inference_slider.get()
    negative_prompt = negative_prompts.get()
    mode = mode_var.get()

    # Create a loading window to indicate progress
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading")
    
    # Center the loading window
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    loading_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Add a label to the loading window
    loading_label = tk.Label(loading_window, text="Generating image...", font=("Helvetica", 14))
    loading_label.pack(expand=True)

    try:
        # Call the external script with subprocess, passing the parameters as arguments
        result = subprocess.run(
            [sys.executable, r'Scripts\inpainting_script.py',
             '--init_image', object_path,
             '--mask_image', mask_path,
             '--prompt', prompt,
             '-show',
             '--n_prompt', negative_prompt,
             '--strength', str(strength),
             '--num_inf', str(inference),
             '--guidance', str(guidance),
             ] + (['-p'] if mode == 'performance' else []),
            capture_output=True,
            text=True,
            check=True
        )
        
        # Show a success message with the result
        messagebox.showinfo("Success", f"Image generated successfully:\n{result.stdout}")

        

    except subprocess.CalledProcessError as e:
        # Handle errors and display an error message
        messagebox.showerror("Error", f"Failed to generate image:\n{e.stderr}")

    finally:
        # Close the loading window after processing
        loading_window.destroy()

# Update the button to call the new function
generate_button = tk.Button(action_frame, text="Generate image", command=on_generate_button_click, font=("Helvetica", 20), bg="lightblue")
generate_button.pack()

# Run the application
root.mainloop()
