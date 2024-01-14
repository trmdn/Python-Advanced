some_text = input()
paren_indexes = []

for index in range(len(some_text)):
    if some_text[index] == "(":
        paren_indexes.append(index)
    elif some_text[index] == ")":
        start_index = paren_indexes.pop()
        end_index = index + 1
        print(some_text[start_index:end_index])