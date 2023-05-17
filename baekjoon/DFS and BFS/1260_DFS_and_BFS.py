from collections import deque

def bfs(graph, root):
    visited = []                # have been visited
    queue = deque([root])       # to be visited

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    
    return " ".join(str(i) for i in visited)

def dfs(graph, root):
    visited = []
    stack = deque([root])
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    
    return " ".join(str(i) for i in visited)


n, m, v = list(map(int,input().split()))
lines = [list(map(int, input().split())) for _ in range(m)]
graph = {}

for line in lines:
    n1, n2 = line[0], line[1]

    if n1 not in graph:         # use list instead of set because it will need to be sorted (condition: visit smaller one first)
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
    
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)


print(dfs(graph, v))
print(bfs(graph, v))