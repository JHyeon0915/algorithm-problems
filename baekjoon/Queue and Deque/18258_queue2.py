# Timeout - couldn't solve
# Time complexity must be O(1)
# pop(0) is led to O(n) because every element would move to the next
# For several inputs, sys.stdin.readline better be used instead of input()
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([])
commands = [input() for _ in range(n)]

for command in commands:
    if "push" in command:
            q.append(int(command.split(" ")[1]))
    elif "pop" in command:
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif "size" in command:
        print(len(q))
    elif "empty" in command:
        if len(q):
            print(0)
        else:
            print(1)
    elif "front" in command:
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif "back" in command:
        if len(q):
            print(q[-1])
        else:
            print(-1)