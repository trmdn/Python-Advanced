word = list(input())
reversed_word = []

for i in range(len(word)):
    reversed_word.append(word.pop())

print("".join(reversed_word))