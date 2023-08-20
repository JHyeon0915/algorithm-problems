def dfs(x, y, number):
    if len(number) == 6:
        result.add(number)
        return
        
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, number + grid[ddx][ddy])

grid = [list(map(str, input().split())) for _ in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, grid[i][j])
print(len(result))