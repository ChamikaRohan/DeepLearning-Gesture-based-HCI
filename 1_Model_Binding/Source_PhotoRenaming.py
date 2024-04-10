import os

def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    # Sort the files so that they are renamed in order
    files.sort()

    # Initialize a counter
    count = 1601

    # Iterate through all files
    for file in files:
        # Get the full path of the file
        old_path = os.path.join(directory, file)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(old_path):
            # Split the file name and its extension
            file_name, file_extension = os.path.splitext(file)

            # Construct the new file name
            new_file_name = str(count) + file_extension

            # Construct the new path for the file
            new_path = os.path.join(directory, new_file_name)

            # If the new path already exists, add a suffix to make it unique
            while os.path.exists(new_path):
                count += 1
                new_file_name = str(count) + file_extension
                new_path = os.path.join(directory, new_file_name)

            # Rename the file
            os.rename(old_path, new_path)

            # Increment the counter for the next file
            count += 1

    print("All files renamed successfully!")

# Replace 'your_directory_path' with the path to your directory containing the images
directory_path = r'C:\Users\M\Desktop\train\peace'

# Call the function to rename files in the specified directory
rename_files(directory_path)

