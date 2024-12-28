import os

def rename_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    num_files = len(files)

    # Determine the number of digits based on the number of files
    if num_files == 0:
        return  # No files to rename

    num_digits = len(str(num_files))

    # Rename files
    for idx, file_name in enumerate(files, start=1):
        # Create a new name with the appropriate number of digits
        new_name = f"{str(idx).zfill(num_digits)}{os.path.splitext(file_name)[1]}"

        # Full paths for the old and new file names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

    # Check and process subfolders
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    for subfolder in subfolders:
        rename_files_in_folder(os.path.join(folder_path, subfolder))

# Main function usage
if __name__ == "__main__":
    folder_to_rename = input("Enter the path of the folder to rename: ").strip()

    if os.path.exists(folder_to_rename) and os.path.isdir(folder_to_rename):
        rename_files_in_folder(folder_to_rename)
        print("All files in the folder and subfolders have been renamed.")
    else:
        print("The path does not exist or is not a folder.")
