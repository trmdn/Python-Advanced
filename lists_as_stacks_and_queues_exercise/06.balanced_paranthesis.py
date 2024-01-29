from collections import deque

paranthesis = deque(input())
open_paranthesis = deque()

while paranthesis:
    current_paranthesis = paranthesis.popleft()

    if current_paranthesis in "{[(":
        open_paranthesis.append(current_paranthesis)
    
    elif not open_paranthesis:
        print("NO")
        break
    
    else:
        if f"{open_paranthesis.pop() + current_paranthesis}" not in "()[]{}":
            print("NO")
            break

else:
    print("YES")