f = open("input.txt")
dic = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
score = 0
def rnd(x):
    if x == 4:
        return 1
    return x
for i in f:
    score+=dic[i[2]]
    if dic[i[2]] == dic[i[0]]:
        score+=3
    elif rnd(dic[i[0]]+1) == dic[i[2]]:
        score+=6
print(score)