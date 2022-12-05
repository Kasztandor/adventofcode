values = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
lines = []
f = open("input.txt")
for i in f:
    lines.append(i.rstrip("\n"))
for i in range(int(len(lines)/3)):
    repeat = ""
    for j in lines[i*3]:
        if j in lines[i*3+1] and j in lines[i*3+2]:
            repeat = j
    score += values.index(repeat)
print(score)