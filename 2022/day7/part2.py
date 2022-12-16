f = open("input.txt")
location = "/"
mappe = {} # "folder" in deutsh :p
score = 70000000
longest = 0
for i in f:
    x = i.rstrip("\n")
    if x[0:2] == "$ ":
        x = x[2:]
        if x[0:3] == "cd ":
            x = x[3:]
            if x == "..":
                location = location.split("/")
                if (len(location)>0):
                    del location[-1]
                location = "/".join(location)
                if location == "":
                    location = "/"
            elif x == "/":
                location = "/"
            else:
                if location[-1] != "/":
                    location += "/"
                location += x
                if location.count("/") > longest:
                    longest = location.count("/")
            if location not in mappe:
                mappe[location] = 0
        if x[0:2] == "ls":
            mappe[location] = 0
    else:
        x = x.split(" ")
        if x[0] != "dir":
            mappe[location] += int(x[0])
while longest > 0:
    for i in mappe:
        if i.count("/") == longest and i != "/":
            j = i.split("/")[0:-1]
            x = "/".join(j)
            if x == "":
                x = "/"
            mappe[x] += mappe[i]
    longest -= 1
minimumSize = mappe["/"]-40000000 # 30000000 - 70000000 = -40000000
for i in mappe:
    if mappe[i] >= minimumSize and mappe[i] < score:
        score = mappe[i]
print(score)