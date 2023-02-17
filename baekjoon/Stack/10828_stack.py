n = int(input())
commands = [input() for _ in range(n)]
stack = []

for command in commands:
    if command[0:4] == "push":
        value = int(command.split(" ")[1])
        stack.append(value)
    elif command[0:3] == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif command[0:4] == "size":
        print(len(stack))
    elif command[0:5] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0:3] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])