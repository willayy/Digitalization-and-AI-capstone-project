import tkinter as tk
from tkinter import filedialog, messagebox, ttk, font
import os
import sys
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ImageDB.database import insert_generated_image
import time

# Function to handle file selection
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

def insert_image(image_obj, image_name):
    # Ask the user if they want to save the image in the database
    save_to_db = messagebox.askyesno("Insert Image", "Do you want to save the generated image to the database?")
    
    if save_to_db:
        # Insert the image into the database
        insert_generated_image(image_obj, image_name)
        # Show a success message
        messagebox.showinfo("Image Generated", "The image has been successfully saved to the database.")
    else:
        messagebox.showinfo("Image Not Saved", "The image was not saved to the database.")

   

# Create the main window
root = tk.Tk()
root.title("SKAPA")
root.geometry("800x600")
root.configure(bg="#f0f0f0")

roboto_15 = font.Font(family="Roboto", size=15)
roboto_20 = font.Font(family="Roboto", size=20)
roboto_20_bold = font.Font(family="Roboto", size=20, weight="bold")

# Apply ttk styling with larger font sizes
style = ttk.Style()
style.configure('TButton', font=roboto_20, padding=10)

style.configure('TLabel', font=roboto_20)
style.configure('Bold.TLabel', font=roboto_20_bold)

style.configure('TFrame', background="#f0f0f0")

style.configure('TEntry', font=roboto_20)
style.configure('Small.TEntry', font=roboto_15)

style.configure('TRadiobutton', font=roboto_15)


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
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

# Prompt Section
# Create and place the new label above the text field
prompt_frame = ttk.Frame(main_frame, padding=10)
prompt_frame.grid(row=0, column=0, sticky="ew", pady=10)

# Prompt Section
prompt_label = ttk.Label(prompt_frame, text="Prompt for the image background", style="Bold.TLabel")
prompt_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry = ttk.Entry(prompt_frame, textvariable=entry_var, width=40, font=roboto_15)
entry.grid(row=0, column=1, padx=10, pady=10)


# File selector function
def create_file_selector(frame, label_text, file_path_var, row):
    file_frame = ttk.Frame(frame)
    file_frame.grid(row=row, column=0, sticky="ew", pady=(5, 15))

    # Label and Browse button for the file selector
    file_label = ttk.Label(file_frame, text=label_text, style="TLabel")
    file_label.grid(row=0, column=0, padx=10, sticky="w")

    file_button = ttk.Button(file_frame, text="Browse",
                              command=lambda: open_file_explorer(file_path_var, filename_label), style="TButton")
    file_button.grid(row=0, column=1, padx=5, sticky="e")

    filename_label = ttk.Label(file_frame, text="", font=roboto_15)
    filename_label.grid(row=0, column=2, padx=10, sticky="w")

# Create and place the file selectors
create_file_selector(main_frame, "Select object image", object_file_path, 1)
create_file_selector(main_frame, "Select object image mask", mask_file_path, 2) 

# Sliders and inputs
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=3, column=0, pady=(15, 25), sticky="ew")

# Slider params
slider_params = [
    ("Strength:", 0, 1, 0.01, 0.8),   # Default value for Strength is 0.8
    ("Guidance:", 0, 20, 0.1, 7.5),   # Default value for Guidance is 7.5
    ("Inference:", 0, 500, 1, 50)     # Default value for Inference is 50
]

# Create and place the input fields inside the input frame
for i, (label_text, from_, to, step, default) in enumerate(slider_params):
    # Create and place the label
    label = ttk.Label(input_frame, text=label_text, style="TLabel")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    # Create and place the slider with increased width and set the default value
    slider = ttk.Scale(input_frame, from_=from_, to=to, orient=tk.HORIZONTAL)
    slider.set(default)
    slider.grid(row=i, column=1, padx=10, pady=5, sticky="ew")

    # Assign each slider to a specific variable for later access
    if label_text == "Strength:":
        strength_slider = slider
    elif label_text == "Guidance:":
        guidance_slider = slider
    elif label_text == "Inference:":
        inference_slider = slider

    # Create and place the input field next to the slider
    input_field = ttk.Entry(input_frame, width=5, font=roboto_15, style="Small.TEntry")
    input_field.insert(0, str(default))  # Set the default value in the input field
    input_field.grid(row=i, column=2, padx=10, pady=5, sticky="e")

    # Function to update the slider value when the input field changes
    def update_slider(event, slider=slider, input_field=input_field, step=step, from_=from_, to=to):
        try:
            value = float(input_field.get())
            # Round to the nearest step
            rounded_value = round(round(float(value) / step) * step, 2)
            if from_ <= rounded_value <= to:
                slider.set(rounded_value)
            else:
                input_field.delete(0, tk.END)
                input_field.insert(0, str(slider.get()))
        except ValueError:
            input_field.delete(0, tk.END)
            input_field.insert(0, str(slider.get()))

    # Function to update the input field value when the slider changes
    def update_input_field(value, input_field=input_field, step=step):
        # Round the value to the nearest step
        rounded_value = round(round(float(value) / step) * step, 2)
        input_field.delete(0, tk.END)
        input_field.insert(0, str(rounded_value))

    # Bind the input field to the update function
    input_field.bind("<Return>", update_slider)
    # Bind the slider to the update function
    slider.config(command=update_input_field)


negative_prompt_label = ttk.Label(input_frame, text="Negative Prompts", style="TLabel")
negative_prompt_label.grid(row=len(slider_params), column=0, padx=10, pady=5, sticky="w")

negative_prompts = ttk.Entry(input_frame, width=50, font=roboto_15, style="Small.TEntry")
negative_prompts.grid(row=len(slider_params), column=1, padx=10, pady=5, columnspan=2, sticky="ew")

# Function to adjust slider lengths dynamically
def adjust_slider_lengths():
    # Get the width of the negative_prompts widget
    negative_prompt_width = negative_prompts.winfo_width()
    # Set the length of all sliders to match the width of the negative_prompts field
    strength_slider.config(length=negative_prompt_width)
    guidance_slider.config(length=negative_prompt_width)
    inference_slider.config(length=negative_prompt_width)

# Call the function after the window has been fully rendered
root.after(10, adjust_slider_lengths)

# Create a frame for the checkboxes
checkbox_frame = ttk.Frame(main_frame)
checkbox_frame.grid(row=4, column=0, pady=(10, 20), sticky="ew")

# Create a StringVar to hold the selected mode
mode_var = tk.StringVar(value="performance")

# Create and place the label above the checkboxes
mode_label = ttk.Label(checkbox_frame, text="Select Mode", style="Bold.TLabel")
mode_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Create and place the "Performance mode" checkbox
performance_checkbox = ttk.Radiobutton(checkbox_frame, text="Performance mode",
                                        variable=mode_var, value="performance", style="TRadiobutton")
performance_checkbox.grid(row=1, column=0, padx=10, pady=5)

# Create and place the "Vanilla mode" checkbox
vanilla_checkbox = ttk.Radiobutton(checkbox_frame, text="Vanilla mode", 
                                   variable=mode_var, value="vanilla", style="TRadiobutton")
vanilla_checkbox.grid(row=1, column=1, padx=10, pady=5)

def reset_choises():
    strength_slider.set(0.8)
    guidance_slider.set(7.5)
    inference_slider.set(50)
    negative_prompts.delete(0, tk.END)
    mode_var.set("performance")

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

    
    try:
        # Call the external script with subprocess, passing the parameters as arguments
        result = subprocess.run(
            [sys.executable, inpainting_script_path,
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

# Dynamically set the path to the Scripts folder
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where gui.py is located
scripts_dir = os.path.join(current_dir, '..', 'Scripts')  # Relative path to the Scripts folder

# Path to the inpainting script
inpainting_script_path = os.path.join(scripts_dir, 'inpainting_script.py')

# Action button
action_frame = ttk.Frame(main_frame)
action_frame.grid(row=5, column=0, pady=(15, 20), sticky="ew")

# Update the button to call the new function
generate_button = ttk.Button(action_frame, text="Generate image", command=on_generate_button_click, style="TButton")
generate_button.pack(side=tk.LEFT, padx=20)

to_default_button = ttk.Button(action_frame, text="Reset to Default", command=reset_choises, style="TButton")
to_default_button.pack(side=tk.LEFT, padx=20)

# Run the application
root.mainloop()