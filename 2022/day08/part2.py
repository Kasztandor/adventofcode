f = open("input.txt")
lines = []
visible = []
def howManyTrees(x, y):
    trees = 1
    treeSize = lines[x][y]
    for i in [[1,0],[-1,0],[0,-1],[0,1]]:
        biggestTreeSize = -1
        mul = 0
        xx = x
        yy = y
        while True:
            xx += i[0]
            yy += i[1]
            if xx < 0 or xx > len(lines)-1 or yy < 0 or yy > len(lines[0])-1:
                break
            mul += 1
            if treeSize <= lines[xx][yy]:
                break
        trees *= mul
    return trees
for i in f:
    lines.append(i.rstrip("\n"))
    visible.append([])
    for j in range(len(i.rstrip("\n"))):
        visible[-1].append(0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        visible[i][j] = howManyTrees(i,j)
score = -1
for i in visible:
    i.sort()
    if i[-1] > score:
        score = i[-1]
print(score)