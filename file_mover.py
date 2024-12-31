import os
import shutil
from sys import argv

class FileMover:
    def __init__(self, home_dir: str, dest_dir: str):
        self.home_dir = os.path.normpath(home_dir)
        self.dest_dir = os.path.normpath(dest_dir)

    def move_one_file(self, file_name_with_extension: str) -> None:
        """Move a single file from home_dir to dest_dir."""
        if file_name_with_extension:
            if os.path.exists(self.home_dir) and os.path.exists(self.dest_dir):
                file_source = os.path.join(self.home_dir, file_name_with_extension)
                file_destination = os.path.join(self.dest_dir, file_name_with_extension)

                if os.path.isfile(file_source):
                    try:
                        shutil.move(file_source, file_destination)
                        print(f"✅ File '{file_name_with_extension}' moved successfully from '{self.home_dir}' to '{self.dest_dir}'.")
                    except Exception as e:
                        print(f"❌ Error moving file '{file_name_with_extension}': {e}")
                else:
                    print(f"❌ The file '{file_name_with_extension}' does not exist at '{self.home_dir}'.")
            else:
                print("❌ Either the source or destination directory does not exist.")
        else:
            print("❌ Please enter a valid file name with extension.")

    def move_multiple_files(self, file_name_with_extension: list) -> None:
        """Move multiple files from home_dir to dest_dir."""
        if isinstance(file_name_with_extension, list) and len(file_name_with_extension) > 0:
            if os.path.exists(self.home_dir) and os.path.exists(self.dest_dir):
                for file in file_name_with_extension:
                    file_source = os.path.join(self.home_dir, file)
                    file_destination = os.path.join(self.dest_dir, file)

                    if os.path.isfile(file_source):
                        try:
                            shutil.move(file_source, file_destination)
                            print(f"✅ File '{file}' moved successfully from '{self.home_dir}' to '{self.dest_dir}'.")
                        except Exception as e:
                            print(f"❌ Error moving file '{file}': {e}")
                    else:
                        print(f"❌ The file '{file}' does not exist at '{self.home_dir}'.")
            else:
                print("❌ Either the source or destination directory does not exist.")
        else:
            print("❌ Please enter a valid list of file names with extension.")

    def move_all_files(self) -> None:
        """Move all files from home_dir to dest_dir."""
        if os.path.exists(self.home_dir) and os.path.exists(self.dest_dir):
            for file in os.listdir(self.home_dir):
                file_source = os.path.join(self.home_dir, file)
                file_destination = os.path.join(self.dest_dir, file)

                if os.path.isfile(file_source):
                    try:
                        shutil.move(file_source, file_destination)
                        print(f"✅ File '{file}' moved successfully from '{self.home_dir}' to '{self.dest_dir}'.")
                    except Exception as e:
                        print(f"❌ Error moving file '{file}': {e}")
                else:
                    print(f"❌ The file '{file}' does not exist at '{self.home_dir}'.")
        else:
            print("❌ Either the source or destination directory does not exist.")

if len(argv) > 1:
    home_dir = argv[1]
    dest_dir = argv[2]
    operation = argv[3].lower()

    file_mover = FileMover(home_dir, dest_dir)

    if operation == "1" or operation == "move one file":
        file_name_with_extension = argv[4]
        file_mover.move_one_file(file_name_with_extension)
    elif operation == "2" or operation == "move multiple files":
        file_name_with_extension_list = argv[4].strip('[]').split(',')
        file_name_with_extension_list = [file.strip() for file in file_name_with_extension_list]
        file_mover.move_multiple_files(file_name_with_extension_list)
    elif operation == "3" or operation == "move all files":
        file_mover.move_all_files()
    else:
        print("❌ Invalid operation mode.")
else:
    home_dir = input("Enter the path of the folder where the files are in: ")
    dest_dir = input("Enter the path of the folder where the files will be moved to: ")
    mode = input("Enter the mode of operation \n1. Move one file\n2. Move multiple files\n3. Move all files\n\n")

    file_mover = FileMover(home_dir, dest_dir)

    if mode == "1" or mode.lower() == "move one file":
        file_name_with_extension = input("Enter the name of the file: ")
        file_mover.move_one_file(file_name_with_extension)
    elif mode == "2" or mode.lower() == "move multiple files":
        file_name_with_extension_prompt = input("Enter the names of the files separated by commas: ")
        file_name_with_extension_list = [file.strip() for file in file_name_with_extension_prompt.split(',')]
        file_mover.move_multiple_files(file_name_with_extension_list)
    elif mode == "3" or mode.lower() == "move all files":
        file_mover.move_all_files()
    else:
        print("❌ Invalid mode of operation.")
