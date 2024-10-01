# genimage python script

## Running from terminal

### Generic windows shell

```shell
python genimage.py <prompt> <image_path> <show_image>

# Optionally you can write it like this so it saves the image to any given path

python genimage.py <prompt> <image_path> <show_image> <save_path>

# Example

python genimage.py "A beautiful sunset" "sunset.jpg" true "C:/Users/username/Desktop/sunset.png"
```

### Generic Unix based systems shell

```shell
python3 genimage.py <prompt> <image_path> <show_image>

# Optionally you can write it like this so it saves the image to any given path

python3 genimage.py <prompt> <image_path> <show_image> <save_path>

# Example

python3 genimage.py "A beautiful sunset" "sunset.jpg" true "/home/username/Desktop/sunset.png"
```

## Running from python script

```python


from genimage import generate_image

generate_image("A beautiful sunset", "Path/To/sunset.jpg", show_image="true", save_path="Path/To/sunset.png")

```




