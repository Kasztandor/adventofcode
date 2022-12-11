f = open("input.txt")
cycle = 0
sumSygnalStrength = 0
x = 1
for i in f:
    if i.rstrip("\n") == "noop":
        cycle += 1
        if (cycle-20) % 40 == 0:
            sumSygnalStrength += x*cycle
    else:
        for j in range(2):
            cycle += 1
            if (cycle-20) % 40 == 0:
                sumSygnalStrength += x*cycle
            if j == 1:
                x += int(i.rstrip("\n").lstrip("addx "))
print(sumSygnalStrength)