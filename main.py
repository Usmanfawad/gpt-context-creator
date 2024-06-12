import csv
from pathlib import Path

from file_iterator import iterate_files

# Get the current working directory
current_directory = Path.cwd()
print(f"Current directory: {current_directory}")

# Read directories to exclude from ignore.csv
with open("ignore.csv") as f:
    ignored_files = f.read().split(",")

# Convert ignored directories to Path objects
excluded_dirs = [current_directory / Path(dir.strip()) for dir in ignored_files]

# Read user-defined files from files.csv (as strings)
with open("files.csv") as f:
    user_defined_files = f.read().split(",")

# Trim whitespace and normalize user-defined file names
user_defined_files = [file.strip() for file in user_defined_files]

# List to hold all found file paths
all_files = []

# Iterate through all files in the current directory and its subdirectories
for file_path in iterate_files(current_directory, excluded_dirs):
    all_files.append(file_path)

# Create or clear the context.txt file
context_file_path = current_directory / "context.txt"
context_file_path.write_text("")  # This will clear the file if it exists

# Iterate over all found files and check if they match the user-defined files
for posix_file in all_files:
    # Check if any user-defined file name matches part of the posix_file name
    if any(
        user_defined_file in posix_file.name for user_defined_file in user_defined_files
    ):
        if posix_file.is_file():  # Ensure it's a file
            try:
                # Read the content of the matched file
                content = posix_file.read_text()
                # Append the content to context.txt
                with context_file_path.open("a") as context_file:
                    context_file.write(f"\n\n--- Content of {posix_file} ---\n\n")
                    context_file.write(content)
                    context_file.write("\n\n--- End of content ---\n\n")
                print(f"Appended content from {posix_file} to {context_file_path}")
            except Exception as e:
                print(f"Error reading {posix_file}: {e}")
