f = open("input.txt")
line = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
visited = ["0:0"]
score = 1
moves = {"U": [0,1], "D": [0,-1], "L": [-1,0], "R": [1,0]}
def move(x):
    line[0][0] += moves[x][0]
    line[0][1] += moves[x][1]
    for i in range(1, len(line)):
        ws1 = line[i][0] - line[i-1][0]
        ws2 = line[i][1] - line[i-1][1]
        if abs(ws1) >= 2 or abs(ws2) >= 2:
            line[i][0] = line[i-1][0]
            line[i][1] = line[i-1][1]
            if abs(ws1) >= 2:
                if ws1 > 0:
                    line[i][0] += 1
                elif ws1 < 0:
                    line[i][0] -= 1
            else:
                if ws2 > 0:
                    line[i][1] += 1
                elif ws2 < 0:
                    line[i][1] -= 1
        if i == len(line)-1:
            visited.append(str(line[-1][0])+":"+str(line[-1][1]))
for i in f:
    for _ in range(int(i[2:].rstrip("\n"))):
        move(i[0])
visited.sort()
for i in range(1, len(visited)):
    if visited[i] != visited[i-1]:
        score += 1
print(score) #36