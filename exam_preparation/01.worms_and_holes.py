from collections import deque

worms = [int(element) for element in input().split()]
holes = deque([int(element) for element in input().split()])

all_worms_count = len(worms)
count_matches = 0

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes.popleft()

    if current_worm == current_hole:
        worms.pop()
        count_matches += 1
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if count_matches:
    print(f"Matches: {count_matches}")
else:
    print(f"There are no matches.")

if not worms and count_matches == all_worms_count:
    print(f"Every worm found a suitable hole!")
elif not worms and count_matches < all_worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(element) for element in worms])}")

if not holes:
    print(f"Holes left: none")
else:
    print(f"Holes left: {', '.join([str(element) for element in holes])}")