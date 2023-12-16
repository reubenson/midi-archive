import os
import glob
import urllib.parse


# Define the directory to search
directory = "src/assets"

# Define the pattern to match
pattern = "**/midi/*.mid"

# Get a list of all files that match the pattern
files = glob.glob(os.path.join(directory, pattern))

# print(f'files {files}')

# Iterate over the files and rename them
for file in files:
    file_dir = os.path.dirname(file)
    # Get the old file name
    old_file_name = os.path.basename(file)

    # if old_file_name.endswith('.MID') >= 0:
    if old_file_name.find('%20') >= 0:
        print(f'old_file_name {old_file_name}')

        # Define the new file name
        new_file_name = old_file_name.replace('%20', ' ')
        # new_file_name = old_file_name.replace('.MID', '.mid')
        print(f'new_file_name {new_file_name}')

        # Rename the file
        os.rename(file, os.path.join(file_dir, new_file_name))