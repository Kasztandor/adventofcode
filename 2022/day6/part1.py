f = open("input.txt")
string = f.readline()
for i in range(0, len(string)-3):
    x = [*string[i:i+4]]
    x.sort()
    if x[0]!=x[1] and x[1]!=x[2] and x[2]!=x[3]:
        print(i+4)
        break