import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
commands = [input() for _ in range(n)]
d = deque()

for c in commands:
    if "push_front" in c:
        element = int(c.split()[1])
        d.appendleft(element)
    elif "push_back" in c:
        element = int(c.split()[1])
        d.append(element)
    elif "pop_front" in c:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif "pop_back" in c:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif "size" in c:
        print(len(d))
    elif "empty" in c:
        if d:
            print(0)
        else:
            print(1)
    elif "front" in c:
        if d:
            print(d[0])
        else:
            print(-1)
    elif "back" in c:
        if d:
            print(d[-1])
        else:
            print(-1)
