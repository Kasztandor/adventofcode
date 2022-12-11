f = open("input.txt")
lines = []
visible = []
for i in f:
    lines.append(i.rstrip("\n"))
    visible.append([])
    for j in range(len(i.rstrip("\n"))):
        visible[-1].append(0)
for i in [[1,0],[-1,1]]:
    for j in range(len(lines)):
        treeSize = -1
        for k in range(len(lines[0])):
            if int(lines[j][k*i[0]-i[1]]) > treeSize:
                visible[j][k*i[0]-i[1]] = 1
                treeSize = int(lines[j][k*i[0]-i[1]])
                continue
    for j in range(len(lines[0])):
        treeSize = -1
        for k in range(len(lines)):
            if int(lines[k*i[0]-i[1]][j]) > treeSize:
                visible[k*i[0]-i[1]][j] = 1
                treeSize = int(lines[k*i[0]-i[1]][j])
                continue
score = 0
for i in visible:
    score += i.count(1)
print(score)