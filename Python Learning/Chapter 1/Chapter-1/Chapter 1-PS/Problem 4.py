import os

def print_directory_contents(path):
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Error: {e}")

directory_path = "Python"  
print_directory_contents(directory_path)
