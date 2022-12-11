f = open("input.txt")
dic = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 1, "Z": 2}
score = 0
def rnd(x):
    if x == 4:
        return 1
    if x == 0:
        return 3
    return x
for i in f:
    score+=dic[i[2]]*3+rnd(dic[i[0]]+dic[i[2]]-1)
print(score)
