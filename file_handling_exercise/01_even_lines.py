symbols = ("-", ",", ".", "!", "?")

with open("file/file_1.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for r in range(0, len(text), 2):
    for symbol in symbols:
        text[r] = text[r].replace(symbol, "@")

    print(text[r][::-1])