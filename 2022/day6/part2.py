f = open("input.txt")
def checkForMultiplications(x):
    x.sort()
    for i in range(1, len(x)):
        if x[i-1]==x[i]:
            return False
    return True
string = f.readline()
for i in range(0, len(string)-13):
    x = [*string[i:i+14]]
    if checkForMultiplications(x):
        print(i+14)
        break