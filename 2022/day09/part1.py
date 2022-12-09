f = open("input.txt")
head = [0,0]
pp = [0,0]
visited = [[0,0]]
moves = {"U": [0,1], "D": [0,-1], "L": [-1,0], "R": [1,0]}
def move(x):
    ppCopy = pp[:]
    pp[0] += moves[x][0]
    pp[1] += moves[x][1]
    if abs(head[0]) + abs(pp[0]) > 2 and abs(head[1]) + abs(pp[1]) > 2:
        head = ppCopy[:]
for i in f:
    visited.append(head[:])
    for _ in range(int(i[2:].rstrip("\n"))):
        move(i[0])
print(visited)