f = open("input.txt")
score = 0
for i in f:
    x = i.rstrip('\n')
    y = x.split(',')
    z = y[0].split('-')+y[1].split('-')
    if int(z[0]) >= int(z[2]) and int(z[1]) <= int(z[3]) or int(z[0]) <= int(z[2]) and int(z[1]) >= int(z[3]):
        score += 1
print(score)