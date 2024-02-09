import os

def create_file(file_name):
    with open(f"files/{file_name}", "w"):
        pass

def add_to_file(file_name, content):
    with open(f"files/{file_name}", "a") as file:
        file.write(f"{content}\n")

def replace_in_file(file_name, old_text, new_text):
    try:
        with open(f"files/{file_name}", "r+") as file:
            text = file.read()
            text = text.replace(old_text, new_text)

            file.seek(0)
            file.write(text)
            file.truncate()
    except FileNotFoundError:
        print("An error occurred!")

def delete_file(file_name):
    try:
        os.remove(f"files/{file_name}")
    except FileNotFoundError:
        print("An error occurred!")

def main():
    while True:
        command, *info = input().split("-")

        if command == "Create":
            create_file(info[0])

        elif command == "Add":
            add_to_file(info[0], info[1])

        elif command == "Replace":
            replace_in_file(info[0], info[1], info[2])

        elif command == "Delete":
            delete_file(info[0])

        elif command == "End":
            break

if __name__ == "__main__":
    main()
