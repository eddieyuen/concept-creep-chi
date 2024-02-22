import os
import shutil

source_folder = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models_tmp'
target_folder = '/Users/kawaiyuen/nlpworkshop/concept-creep-chi_raw/models_final'

# Loop through the years 1979 to 2021
for year in range(1979, 2022):
    # Generate the filename using the year
    filename = f"pd_{year}.model"
    
    # Check if the file exists in the source folder
    source_path = os.path.join(source_folder, filename)
    if os.path.exists(source_path):
        # Move the file to the target folder
        target_path = os.path.join(target_folder, filename)
        shutil.move(source_path, target_path)
        print(f"Moved {filename} to {target_path}")
    else:
        print(f"{filename} not found in the source folder.")

print("File moving completed.")