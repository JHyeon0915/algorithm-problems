n = int(input())
roads = list(map(int,input().split(" ")))
prices = list(map(int,input().split(" ")))
prices.pop()

cost = 0
index = 0

while(True):
    currentPrice = prices[index]

    while currentPrice <= prices[index]:
        cost += currentPrice * roads[index]
        index += 1
        if len(roads) == index:
            print(cost)
            exit()
