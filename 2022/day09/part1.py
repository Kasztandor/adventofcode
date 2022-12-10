f = open("input.txt")
line = [[0,0],[0,0]]
visited = ["0:0"]
score = 1
moves = {"U": [0,1], "D": [0,-1], "L": [-1,0], "R": [1,0]}
def move(x):
    line[1-1][0] += moves[x][0]
    line[1-1][1] += moves[x][1]
    if abs(line[1][0] - line[1-1][0]) >= 2 or abs(line[1][1] - line[1-1][1]) >= 2:
        line[1][0] = line[1-1][0]-moves[x][0]
        line[1][1] = line[1-1][1]-moves[x][1]
        visited.append(str(line[1][0])+":"+str(line[1][1]))
for i in f:
    for _ in range(int(i[2:].rstrip("\n"))):
        move(i[0])
visited.sort()
for i in range(len(visited)):
    if i > 0 and visited[i] != visited[i-1]:
        score += 1
print(score)