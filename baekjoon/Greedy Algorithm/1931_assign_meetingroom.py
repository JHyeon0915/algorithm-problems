# couldn't solve
# Sort the schedules by startime ascending order 
# Sort it again by endtime with ascending order 
# When startime is the same for bigger than entime, max + 1

n = int(input())
schedules = []

for _ in range(n):
    schedules.append(list(map(int, input().split())))

# sort by end time descending
schedules.sort()
print(schedules)

schedules.sort(key = lambda x: (x[1],x[0]))
print(schedules)

max = 1
endTime = schedules[0][1]

for i in range(1, n):
    if schedules[i][0] >= endTime:
        max += 1
        endTime = schedules[i][1]

print(max)