from PIL import Image
import os

def resize_images(directory, new_width=28, new_height=28):
    # Get list of all files in directory
    files = os.listdir(directory)

    # Iterate over each file in the directory
    for filename in files:
        # Construct full path to the file
        file_path = os.path.join(directory, filename)
        
        # Check if the file is an image
        if os.path.isfile(file_path) and any(filename.lower().endswith(image_ext) for image_ext in ['.jpg', '.jpeg', '.png', '.bmp']):
            # Open the image
            img = Image.open(file_path)
            
            # Resize the image
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            
            # Save the resized image, overwriting the original file
            img.save(file_path)

# Example usage:
directory = 'D:/NGUYEN/CV_ML/Dataset/PokemonImages28gray'
resize_images(directory)
