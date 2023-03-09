import sys
import heapq      # 최소힙만 지원

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    i = int(input())
    if i == 0:
        if heap:
            print((-1) * heapq.heappop(heap))   # - 를붙이면 최대값이 최소값이 됨
        else:
            print(0)
    else:
        heapq.heappush(heap,(-1) * i)