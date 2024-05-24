import os
from PIL import Image

def convert_images_to_gray(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Create a new folder to save the grayscale images
    gray_folder_path = os.path.join(folder_path, 'grayscale_images')
    os.makedirs(gray_folder_path, exist_ok=True)

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Open an image file
            with Image.open(file_path) as img:
                # Convert image to grayscale
                gray_img = img.convert('L')
                
                # Save the grayscale image to the new folder
                gray_img_path = os.path.join(gray_folder_path, filename)
                gray_img.save(gray_img_path)
                print(f"Converted '{filename}' to grayscale and saved as '{gray_img_path}'.")

folder_path = 'D:/NGUYEN/CV_ML/Pokemon128gray'
convert_images_to_gray(folder_path)
