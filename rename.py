import os
import shutil

def rename_images(directory):
    # Get list of all files in directory
    files = os.listdir(directory)
    
    # Sort files to ensure consistent ordering
    files.sort()
    
    # Rename each file sequentially
    for index, filename in enumerate(files, start=1):
        # Get file extension
        extension = os.path.splitext(filename)[1]
        
        # Generate new filename
        new_filename = str(index) + extension
        
        # Construct full paths
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        
        # Rename file
        os.rename(old_path, new_path)

# Example usage:
directory = 'D:/NGUYEN/CV_ML/PokemonImages'
rename_images(directory)
