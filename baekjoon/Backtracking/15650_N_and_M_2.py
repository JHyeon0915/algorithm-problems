n, m = list(map(int, input().split())) # 4 2
l = []
setList = []

def dfs():
    if len(l) == m and set(l) not in setList:
        print(' '.join(map(str, l)))
        setList.append(set(l))
        return
    
    for i in range(1,n+1):
        if i not in l:
            l.append(i)
            dfs()
            l.pop()         # pop i
        
dfs()