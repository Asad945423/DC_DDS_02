<<<<<<< HEAD
import os

def print_dir_structure(root_dir, output_file, exclude_dirs=None, indent=""):
    if exclude_dirs is None:
        exclude_dirs = []
    try:
        items = sorted(os.listdir(root_dir))
        for item in items:
            item_path = os.path.join(root_dir, item)
            if item in exclude_dirs:
                continue
            # Write item, replacing unprintable characters
            try:
                output_file.write(f"{indent}├── {item}\n")
            except UnicodeEncodeError:
                output_file.write(f"{indent}├── [Unprintable: {repr(item)}]\n")
            if os.path.isdir(item_path):
                print_dir_structure(item_path, output_file, exclude_dirs, indent + "│   ")
    except PermissionError:
        output_file.write(f"{indent}├── [Permission Denied]\n")
    except OSError as e:
        output_file.write(f"{indent}├── [Error: {str(e)}]\n")

# Example usage
app_path = "D:/lms"  # Use forward slashes
exclude = ["node_modules"]
with open("structure.txt", "w", encoding="utf-8") as f:
    f.write(f"Directory structure of {app_path}:\n")
=======
import os

def print_dir_structure(root_dir, output_file, exclude_dirs=None, indent=""):
    if exclude_dirs is None:
        exclude_dirs = []
    try:
        items = sorted(os.listdir(root_dir))
        for item in items:
            item_path = os.path.join(root_dir, item)
            if item in exclude_dirs:
                continue
            # Write item, replacing unprintable characters
            try:
                output_file.write(f"{indent}├── {item}\n")
            except UnicodeEncodeError:
                output_file.write(f"{indent}├── [Unprintable: {repr(item)}]\n")
            if os.path.isdir(item_path):
                print_dir_structure(item_path, output_file, exclude_dirs, indent + "│   ")
    except PermissionError:
        output_file.write(f"{indent}├── [Permission Denied]\n")
    except OSError as e:
        output_file.write(f"{indent}├── [Error: {str(e)}]\n")

# Example usage
app_path = "D:/lms"  # Use forward slashes
exclude = ["node_modules"]
with open("structure.txt", "w", encoding="utf-8") as f:
    f.write(f"Directory structure of {app_path}:\n")
>>>>>>> 3151975b (Initals)
    print_dir_structure(app_path, f, exclude)