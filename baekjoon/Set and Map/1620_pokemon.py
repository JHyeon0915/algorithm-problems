n, m = list(map(int, input().split(" ")))
result = []
d_key = {}
d_val = {}

for i in range(1,n+1):
    s = input()
    d_key[s] = i
    d_val[i] = s

t = (input() for i in range(m))

for _ in range(m):
    i = input()
    if i.isdigit():
        result.append(d_val[int(i)])
    else:
        result.append(d_key[i])

for i in result:
    print(i)