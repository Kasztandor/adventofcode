f = open("input.txt")
calories = [0]
for i in f:
    if i == "\n":
        calories.append(0)
    else:
        calories[-1]+=int(i.rstrip(i[-1]))
calories.sort()
print(calories[-1]+calories[-2]+calories[-3])