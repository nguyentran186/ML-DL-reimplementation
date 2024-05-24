import os
import shutil

def collect_images(source_dir, target_dir, image_extensions=['.jpg', '.jpeg', '.png', '.gif', '.bmp']):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_dir, file)
                
                # Ensure unique filenames to avoid overwriting
                if os.path.exists(target_file):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    new_target_file = f"{base}_{counter}{ext}"
                    while os.path.exists(os.path.join(target_dir, new_target_file)):
                        counter += 1
                        new_target_file = f"{base}_{counter}{ext}"
                    target_file = os.path.join(target_dir, new_target_file)
                
                shutil.copy2(source_file, target_file)
                print(f"Copied {source_file} to {target_file}")

source_directory = 'D:/NGUYEN/CV_ML/PokemonImagesDB' 
target_directory = 'D:/NGUYEN/CV_ML/PokemonImages'

collect_images(source_directory, target_directory)
