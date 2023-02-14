n = int(input())
time = list(map(int, input().split()))

time.sort()

total = 0
for i in range(len(time)):
    total += time[i] * (len(time) - i)

print(total)