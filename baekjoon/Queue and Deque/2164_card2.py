import sys

front = -1
n = int(input())
cards = [i for i in range(1, n+1)]
answer = 0

if n == 1:
    print(1)
    exit(0)

while(True):
    front += 1
    if cards[front+1] == cards[-1]:
        answer = cards[-1]
        break
    cards.append(cards[front+1])
    front += 1

print(answer)