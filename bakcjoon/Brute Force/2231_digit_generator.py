digitsum = int(input())
generator = 0

def getUnits(n):
    u = 1
    units = 10
    while(True):
        if (n - units**u) < 0:
            break
        u = u+1

    if u == 1:
        return n
    return getGen(n,u-1)

def getGen(n, u):
    r = int(n / (10**u))
    n = n - (r * 10**u)

    if(n == 0):
        return r
    return r + getGen(n,u-1)

for i in range(1,digitsum):
    if (i + getUnits(i)) == digitsum:
        generator = i
        break

print(generator)