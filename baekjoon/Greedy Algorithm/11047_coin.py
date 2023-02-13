n, k = list(map(int, input().split()))
values = []
cnt = 0

for _ in range(n):
    values.append(int(input()))

values.reverse()

for value in values:
    if value > k:
        continue

    quotient = int(k / value)
    k = k % value
    cnt = cnt + quotient

    if k ==0:
        break

print(cnt)

