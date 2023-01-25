n, m = list(map(int, input().split(" ")))
cnt = 0
s = set()

for i in range(n):
    s.add(input())

for i in range(m):
    e = input()
    if e in s:
        cnt = cnt + 1

print(cnt)