import os

def print_directory_contents(path):
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
directory_path = "."  # Current directory
print_directory_contents(directory_path)