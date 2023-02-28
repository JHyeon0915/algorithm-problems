s = input()
storage = set()

for i in range(len(s)):
    k = 0
    for j in range(len(s)-i):
        storage.add(s[k:j+i+1])
        k += 1

print(len(storage))
