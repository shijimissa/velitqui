# Import the 'os' module to access operating system functionalities.
import os

# Define the path to a file or directory.
path = "abc.txt"

# Check if the path refers to a directory.
if os.path.isdir(path):
    # Print a message indicating that it is a directory.
    print("\nIt is a directory")
# Check if the path refers to a regular file.
elif os.path.isfile(path):
    # Print a message indicating that it is a normal file.
    print("\nIt is a normal file")
# If the path doesn't match a directory or a regular file, assume it's a special file (e.g., socket, FIFO, device file).
else:
    # Print a message indicating that it is a special file.
    print("It is a special file (socket, FIFO, device file)")
# Print a newline character for spacing.
print()
