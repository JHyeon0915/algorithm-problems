expression = input()
operations = {}

for i in range(len(expression)):
    if expression[i] == '+' or expression[i] == '-':
        operations[i] = expression[i]

operations[len(expression)] = "end"

minus = False
keys = list(operations.keys())
answer = int(expression[ 0 : keys[0] ])

for i in range(len(keys) - 1):
    start = keys[i]+1
    end = keys[i+1]
    operation = operations[keys[i]]

    if operation == '-':
        minus = True

    if minus:
        answer = answer - int(expression[start:end])
        start = end
        continue

    answer += int(expression[start:end])
    start = end

print(answer)