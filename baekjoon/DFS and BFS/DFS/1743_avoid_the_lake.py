import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, K = list(map(int, input().split(' ')))
farm = [[0 for _ in range(M+1)] for _ in range(N+1)]
lakes = [list(map(int, input().split(' '))) for _ in range(K)]

for lake in lakes:
    farm[lake[0]][lake[1]] = 1

visited = [[False]*(M+1) for _ in range(N+1)]       # faster than visited = []
def dfs(lake):
    max = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    if lake not in visited:
        visited[lake[0]][lake[1]] = True

    for i in range(4):
        ddx = lake[0]+dx[i]
        ddy = lake[1]+dy[i]
        if ddx > 0 and ddx < N+1 and ddy > 0 and ddy < M+1 and farm[ddx][ddy] and not visited[ddx][ddy]:
            visited[ddx][ddy] = True
            max += dfs([ddx, ddy])

    return max

print(max([dfs(lake) for lake in lakes if not visited[lake[0]][lake[1]]]))
