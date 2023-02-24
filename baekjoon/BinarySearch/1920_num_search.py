import sys
input = sys.stdin.readline

n = int(input())
nList = set(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

for e in mList:
    if e in nList:
        print(1)
    else:
        print(0)