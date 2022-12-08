f = open("day8/inp.txt")
lines = []
visible = []
def howManyTrees(x, y):
    trees = 0
    #treeSize = lines[x][y]
    for i in [[1,0],[-1,0],[0,-1],[0,1]]:
        xx = x
        yy = y
        biggestTreeSize = 0
        while True:
            xx += i[0]
            yy += i[1]
            if xx < 0 or xx > len(lines)-1 or yy < 0 or yy > len(lines[0])-1:
                break
            if int(lines[xx][yy]) >= biggestTreeSize:
                trees += 1
                biggestTreeSize = int(lines[xx][yy])
    return trees
for i in f:
    lines.append(i.rstrip("\n"))
    visible.append([])
    for j in range(len(i.rstrip("\n"))):
        visible[-1].append(howManyTrees(len(visible)-1,j))
#score = 0
for i in visible:
    i.sort()
    for j in i:
        print(j, end=" ")
    print()
    #score = i[-1]
#print(score)