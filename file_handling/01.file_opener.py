import os

ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
file_name = "test.txt"
path = os.path.join("..", "..", "nested-folde_", "file_name")

try:
    file = open("test.txt", "r")
    print("File found")
except FileNotFoundError:
    print("File is not found")