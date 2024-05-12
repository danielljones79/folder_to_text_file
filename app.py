import os

def traverse_folder(folder_path):
    output_file = "output.txt"
    with open(output_file, "w") as f:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                f.write(f"---- File Name: \"{relative_path}\" ----\n")
                try:
                    with open(file_path, 'rb') as file_content:
                        content = file_content.read()
                    try:
                        # Try decoding as UTF-8
                        content_decoded = content.decode('utf-8')
                    except UnicodeDecodeError:
                        # If decoding fails, replace non-decodable parts
                        content_decoded = content.decode('utf-8', errors='replace')
                    f.write(content_decoded + "\n")
                except Exception as e:  # catch any reading errors
                    print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
    else:
        traverse_folder(sys.argv[1])
