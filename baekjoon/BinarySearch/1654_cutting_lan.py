# Use upper bound
# Upper bound: return the location that first exceeds the target
# Lower bound: return the location that is first bigger value than the target
# These concepts are important when there are redundant values

import sys
input = sys.stdin.readline

n,m = list(map(int, input().split()))
lengths = [int(input()) for _ in range(n)]

low = 0
high = max(lengths)+1       # max shoud be one plused
mid = 0

while(low<high):
    mid = int((low + high)/2)
    sumCount = sum([int(l/mid) for l in lengths])
    if m > sumCount:
        high = mid
    else:
        low = mid+1

print(low - 1)