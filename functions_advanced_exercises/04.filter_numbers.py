def even_odd_filter(**number_sets):
    if "odd" in number_sets:
        number_sets["odd"] = [num for num in number_sets["odd"] if num % 2 != 0]
    elif "even" in number_sets:
        number_sets["even"] = [num for num in number_sets["even"] if num % 2 == 0]

    return dict(sorted(number_sets.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))