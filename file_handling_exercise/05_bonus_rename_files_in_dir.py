import os
import re

def replace_string_in_files(directory, string_to_replace, string_to_replace_with):
    for file_name in os.listdir(directory):
        file = os.path.join(directory, file_name)

        if os.path.isfile(file):
            new_name = file_name.replace(string_to_replace, string_to_replace_with)
            new_file = os.path.join(os.path.dirname(file), new_name)
            os.rename(file, new_file)

def main():
    directory = input("Enter a directory: ")
    string_to_replace = input("Enter a string to replace: ")
    string_to_replace_with = input("Enter a string to replace with: ")

    replace_string_in_files(directory, string_to_replace, string_to_replace_with)

if __name__ == "__main__":
    main()
