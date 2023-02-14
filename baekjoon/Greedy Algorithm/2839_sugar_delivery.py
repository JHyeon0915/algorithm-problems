# couldn't solve
# kg - 3 and count it till kg can be divided by 5

kg = int(input())
cnt = 0

while(True):
    if kg%5 == 0:
        cnt = cnt + int(kg/5)
        break
    kg = kg - 3
    if(kg < 0):
        cnt = -1
        break
    cnt = cnt + 1

print(cnt)