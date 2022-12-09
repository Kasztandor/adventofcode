f = open("input.txt")
head = [0,0]
pp = [0,0] # player position you perv
visited = ["0:0"]
score = 1
moves = {"U": [0,1], "D": [0,-1], "L": [-1,0], "R": [1,0]}
def move(x):
    ppCopy = pp[:]
    pp[0] += moves[x][0]
    pp[1] += moves[x][1]
    if abs(head[0] - pp[0]) >= 2 or abs(head[1] - pp[1]) >= 2:
        head[0] = ppCopy[0]
        head[1] = ppCopy[1]
        visited.append(str(head[0])+":"+str(head[1]))
for i in f:
    for _ in range(int(i[2:].rstrip("\n"))):
        move(i[0])
visited.sort()
for i in range(len(visited)):
    if i > 0 and visited[i] != visited[i-1]:
        score += 1
print(score)