n, m = list(map(int, input().split())) # 4 2
l = []

def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1,n+1):
        if i not in l:
            l.append(i)
            dfs()
            l.pop()         # pop i
        
dfs()