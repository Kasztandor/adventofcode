f = open("input.txt")
score = 0
def ranger(x,y):
    ret = []
    for i in range(x,y+1):
        ret.append(i)
    return ret
for i in f:
    x = i.rstrip('\n')
    y = x.split(',')
    z = y[0].split('-')+y[1].split('-')
    addscore = 0
    for i in ranger(int(z[0]),int(z[1])):
        for j in ranger(int(z[2]),int(z[3])):
            if i == j:
                addscore = 1
    score += addscore
print(score)