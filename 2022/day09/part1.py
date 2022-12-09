f = open("input.txt")
line = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
visited = ["0:0"]
score = 1
moves = {"U": [0,1], "D": [0,-1], "L": [-1,0], "R": [1,0]}
def move(x):
    for i in range(1, len(line)):
        line[i-1][0] += moves[x][0]
        line[i-1][1] += moves[x][1]
        if abs(line[i][0] - line[i-1][0]) >= 2 or abs(line[i][1] - line[i-1][1]) >= 2:
            line[i][0] = line[i-1][0]-moves[x][0]
            line[i][1] = line[i-1][1]-moves[x][1]
            if i == len(line)-1:
                visited.append(str(line[i][0])+":"+str(line[i][1]))
for i in f:
    for _ in range(int(i[2:].rstrip("\n"))):
        move(i[0])
visited.sort()
for i in range(len(visited)):
    if i > 0 and visited[i] != visited[i-1]:
        score += 1
print(score)