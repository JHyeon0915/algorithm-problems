n, m = list(map(int, input().split(" ")))
cnt = 0
l = []
for i in range(n):
    l.append(input())

for i in range(m):
    string = input()
    for j in l:
        if string == j:
            cnt = cnt + 1
            break

print(cnt)