n = int(input())
stack = [0,]
for i in range(n):
    e = int(input())
    if e == 0:
        stack.pop()
    else:
        stack.append(e)

print(sum(stack))