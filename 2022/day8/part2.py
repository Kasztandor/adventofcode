f = open("input.txt")
lines = []
visible = []
def howManyTrees(x, y):
    trees = 1
    treeSize = lines[x][y]
    for i in [[1,0],[-1,0],[0,-1],[0,1]]:
        treeSize = lines[x][y]
    return trees
for i in f:
    lines.append(i.rstrip("\n"))
    visible.append([])
    for j in range(len(i.rstrip("\n"))):
        visible[-1].append(howManyTrees(len(visible)-1,j))
score = 0
for i in visible:
    i.sort()
    score = i[-1]
print(score)