f = open("input.txt")
lines = []
stacks = []
for i in f:
    lines.append(i.rstrip("\n"))
stacksNo = lines[lines.index("")-2].count("[")
for i in range(stacksNo):
    stacks.append([])
for i in range(lines.index("")-2, -1, -1):
    for j in range(stacksNo):
        if lines[i][4*j+1] != " ":
            stacks[j].append(lines[i][4*j+1])
for i in range(lines.index("")+1):
    del lines[0]
for i in lines:
    x = i.replace("move ","").replace("from ","").replace("to ","").split(" ")
    x = [int(x[0]),int(x[1]),int(x[2])]
    for j in range(x[0]):
        stacks[x[2]-1].append(stacks[x[1]-1].pop(j-x[0]))
for i in stacks:
    print(i[-1],end="")