from string import punctuation

def count_letters_and_marks(line):
    letters, marks = 0, 0
    for symbol in line:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1
    return letters, marks

def process_file(input_path, output_path):
    with open(input_path, "r") as text_file:
        text = text_file.readlines()

    with open(output_path, "w") as output_file:
        for r, line in enumerate(text, start=1):
            letters, marks = count_letters_and_marks(line[:-1])
            output_file.write(f"Line {r}: {line[:-1]} ({letters}) {marks}\n")

# Replace the file paths with your actual file paths
input_file_path = "files/file_1.txt"
output_file_path = "files/output_2.txt"

process_file(input_file_path, output_file_path)
