import os

def delete_even_named_images(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file name without the extension
            name, ext = os.path.splitext(filename)
            
            # Check if the name is numeric and even
            if name.isdigit() and int(name) % 2 == 1:
                # Delete the file
                os.remove(file_path)
                print(f"Deleted '{filename}'.")

folder_path = 'D:/NGUYEN/CV_ML/dataset/Pokemon28gray'
delete_even_named_images(folder_path)
