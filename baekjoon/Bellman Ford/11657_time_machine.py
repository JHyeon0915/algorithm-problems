import sys
input  = sys.stdin.readline
INF = 10 ** 18
minusCycle = False

v, e = list(map(int,input().split()))

dist = [INF for _ in range(v)]
adj = [[] for _ in range(v)]

for i in range(e):
    city1, city2, cost = list(map(int, input().split()))
    adj[city1-1].append((city2-1, cost))

dist[0] = 0

for i in range(v):
    for j in range(v):
        for k in range(len(adj[j])):
            next, d = adj[j][k]
            if dist[j] != INF and dist[next] > dist[j]+d:
                dist[next] = dist[j] + d
                if i == (v - 1):
                    minusCycle = True

if minusCycle:
        print("-1")
else:
    for i in range(1, v):
        if dist[i] < INF:
            print(dist[i])
        else:
            print("-1")
