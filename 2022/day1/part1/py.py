f = open("input.txt")
current = 0
high = 0
for i in f:
    if i == "\n":
        current = 0
    else:
        current += int(i.rstrip(i[-1]))
    if current > high:
        high = current
print(high)