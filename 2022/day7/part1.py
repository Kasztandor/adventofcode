f = open("input.txt")
location = "/"
for i in f:
    x = i.rstrip("\n")
    if x[0:2] == "$ ":
        x = x.lstrip("$ ")
        if x[0:3] == "cd ":
            x = x.lstrip("cd ")
            if x == "..":
                location = location.split("/")
                if (len(location)>0):
                    del location[-1]
                location = "/".join(location)
            elif x == "/":
                location = "/"
            else:
                if location[-1] != "/":
                    location += "/"
                location += x
            print(location)