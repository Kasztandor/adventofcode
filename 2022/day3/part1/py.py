values = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
f = open("input.txt")
for i in f:
    x = i.replace("\n","")
    repeates = ""
    for j in range(int(len(x)/2)):
        for k in range(int(len(x)/2)):
            if x[j]==x[int(len(x)/2)+k]:
                repeates+=x[j]
    letters = ""
    for j in repeates:
        if not (j in letters):
            letters+=j
            score+=values.index(j)
print(score)