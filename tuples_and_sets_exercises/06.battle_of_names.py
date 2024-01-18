odd_names = set()
even_names = set()
number = int(input())

for row in range(1, number + 1):
    ascii_num_of_name = sum(ord(z) for z in input()) // row

    if ascii_num_of_name % 2 == 0:
        even_names.add(ascii_num_of_name)
    else:
        odd_names.add(ascii_num_of_name)

sum_odd_set, sum_even_set = sum(odd_names), sum(even_names)

if sum_even_set == sum_odd_set:
    print(*odd_names.union(even_names), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_names.difference(even_names), sep=", ")
else:
    print(*odd_names.symmetric_difference(even_names), sep=", ")