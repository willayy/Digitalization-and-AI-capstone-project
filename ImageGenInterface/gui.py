import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
from PIL import Image
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ImageDB.database import insert_generated_image

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
    loading_window.configure(bg="#f0f0f0")
    
    # Centering the loading window on the screen
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    loading_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # Adding a label to the loading window 
    loading_label = tk.Label(loading_window, text="Generating image...", font=("Roboto", 14), bg="#f0f0f0")
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
root.geometry("800x600")
root.configure(bg="#f0f0f0")

# Apply ttk styling with larger font sizes
style = ttk.Style()
style.configure('TButton', font=('Roboto', 20), padding=10)
style.configure('TLabel', font=('Roboto', 20))
style.configure('TFrame', background="#f0f0f0")
style.configure('TEntry', font=('Roboto', 20))
style.configure('TScale', sliderlength=30, length=300)
style.configure('TRadiobutton', font=('Roboto', 15))


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

# Create and place the new label above the text field
prompt_label = ttk.Label(prompt_frame, text="Write a prompt for the image background")
prompt_label.pack(anchor="n", pady=(0, 5))

# Create and place the text field inside the main frame
entry = ttk.Entry(prompt_frame, textvariable=entry_var, width=60, style="TEntry")
entry.pack(anchor="n")

# File selector function
def create_file_selector(frame, label_text, file_path_var, row):
    file_frame = ttk.Frame(frame)
    file_frame.grid(row=row, column=0, columnspan=2, pady=(20, 10))

    # Label and Browse button for the file selector
    file_label = ttk.Label(file_frame, text=label_text)
    file_label.pack(side=tk.LEFT, padx=10)

    file_button = ttk.Button(file_frame, text="Browse", command=lambda: open_file_explorer(file_path_var, filename_label))
    file_button.pack(side=tk.LEFT)

    filename_label = ttk.Label(file_frame, text="")
    filename_label.pack(side=tk.LEFT, padx=10)

# Create and place the file selectors
create_file_selector(main_frame, "Select object image", object_file_path, 1)
create_file_selector(main_frame, "Select object image mask", mask_file_path, 2)

# Sliders and inputs
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=3, column=0, pady=(10, 20))

# Slider params
slider_params = [
    ("Strength", 0, 1, 0.01, 0.8),   # Default value for Strength is 0.8
    ("Guidance", 0, 20, 0.1, 7.5),   # Default value for Guidance is 7.5
    ("Inference", 0, 500, 1, 50)     # Default value for Inference is 50
]

# Create and place the input fields inside the input frame
for i, (label_text, from_, to, step, default) in enumerate(slider_params):
    # Create and place the label
    label = ttk.Label(input_frame, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    
    # Create and place the slider with increased width and set the default value
    slider = ttk.Scale(input_frame, from_=from_, to=to, orient=tk.HORIZONTAL)
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
    input_field = ttk.Entry(input_frame)
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


negative_prompt_label = ttk.Label(input_frame, text="Negative Prompts")
negative_prompt_label.grid(row=len(slider_params), column=0, padx=10, pady=5, sticky="w")

negative_prompts = ttk.Entry(input_frame)
negative_prompts.grid(row=len(slider_params), column=1, padx=10, pady=5)

# Create a frame for the checkboxes
checkbox_frame = ttk.Frame(main_frame)
checkbox_frame.grid(row=4, column=0, columnspan=3, pady=(10, 20))

# Create a StringVar to hold the selected mode
mode_var = tk.StringVar(value="performance")

# Create and place the label above the checkboxes
mode_label = ttk.Label(checkbox_frame, text="Select Mode")
mode_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Create and place the "Performance mode" checkbox
performance_checkbox = ttk.Radiobutton(checkbox_frame, text="Performance mode", variable=mode_var, value="performance")
performance_checkbox.grid(row=1, column=0, padx=10, pady=5)

# Create and place the "Vanilla mode" checkbox
vanilla_checkbox = ttk.Radiobutton(checkbox_frame, text="Vanilla mode", variable=mode_var, value="vanilla")
vanilla_checkbox.grid(row=1, column=1, padx=10, pady=5)

# Action button
action_frame = ttk.Frame(main_frame)
action_frame.grid(row=5, column=0, columnspan=2, pady=(10, 20)) 

def on_generate_button_click():
    # Get values from the UI elements
    prompt = entry_var.get()  # Prompt for the image
    object_path = object_file_path.get()  # Object image file path
    mask_path = mask_file_path.get()  # Mask file path
    strength = strength_slider.get()  # Strength slider value
    guidance = guidance_slider.get()  # Guidance slider value
    inference = inference_slider.get()  # Inference slider value
    negative_prompt = negative_prompts.get()  # Negative prompts text
    mode = mode_var.get()  # Selected mode (performance or vanilla)

    # Call the image generation function with the collected values
    start_image_generation(
        prompt, object_path, mask_path, strength, guidance, inference, negative_prompt, mode
    )

# Update the button to call the new function
generate_button = ttk.Button(action_frame, text="Generate image", command=on_generate_button_click)
generate_button.pack()

# Run the application
root.mainloop()