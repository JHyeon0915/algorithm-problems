n, m = map(int,input().split(" "))
cards = list(map(int,input().split(" ")))
gap = m
result = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = cards[i]+cards[j]+cards[k]
            if (sum <= m) and ((m - sum) < gap):
                gap = m - sum
                result = sum

print(result)