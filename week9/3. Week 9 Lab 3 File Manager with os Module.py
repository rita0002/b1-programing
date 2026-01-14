import os

def file_manager():
    """
    demonstration of file and folder operations
    using the os module.
    """

    # 1. Show the current working directory
    current_directory = os.getcwd()
    print("Current Working Directory:")
    print(current_directory)
    print()

    # 2. Create a new folder called 'lab_files'
    folder_name = "lab_files"

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder created: {folder_name}")
    else:
        print(f"Folder already exists: {folder_name}")

    print()

    # 3. Create three text files inside the folder
    file_list = ["file1.txt", "file2.txt", "file3.txt"]

    for filename in file_list:
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "w") as file:
            file.write(f"This is {filename}")
        print(f"File created: {filename}")

    # 4. List all files in the folder
    print("\nFiles inside the folder:")
    for file in os.listdir(folder_name):
        print("-", file)

    # 5. Rename one file
    old_file = os.path.join(folder_name, "file2.txt")
    new_file = os.path.join(folder_name, "renamed_file.txt")

    if os.path.exists(old_file):
        os.rename(old_file, new_file)
        print("\nFile renamed: file2.txt → renamed_file.txt")

    # Show files after renaming
    print("\nFiles after renaming:")
    for file in os.listdir(folder_name):
        print("-", file)

    # 6. Clean up: delete files and remove folder
    print("\nCleaning up files and folder...")
    for file in os.listdir(folder_name):
        os.remove(os.path.join(folder_name, file))
        print(f"Deleted file: {file}")

    os.rmdir(folder_name)
    print(f"Folder removed: {folder_name}")

    print("\nFile management demo completed successfully!")

# Run the program
file_manager()

