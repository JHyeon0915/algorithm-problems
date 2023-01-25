n = int(input())
cards = list(map(int, input().split(" ")))
m = int(input())
nums = list(map(int, input().split(" ")))

dc = {}
dn = {}

for i in cards:
    dc[i] = 1
for i in nums:
    dn[i] = 0

for i in dn.keys():
    try:
        dc[i]
        dn[i] = 1
    except:
        continue

for i in dn.values():
    print(i, end=" ")
