from math import floor
f = open("input.txt")
cycle = 0
sumSygnalStrength = 0
x = 1
screen = [[]]
def draw():
    if cycle%40 == 0:
        screen.append([])
    if x in [cycle-1-40*floor(cycle/40), cycle-40*floor(cycle/40), cycle+1-40*floor(cycle/40)]:
        screen[-1].append("#")
    else:
        screen[-1].append(".") # I left this same as in task, but for me space is better to read screen output, so i recomend to change it when you wanna run the code.
for i in f:
    if i.rstrip("\n") == "noop":
        draw()
        cycle += 1
        if (cycle-20) % 40 == 0:
            sumSygnalStrength += x*cycle
    else:
        for j in range(2):
            draw()
            cycle += 1
            if (cycle-20) % 40 == 0:
                sumSygnalStrength += x*cycle
            if j == 1:
                x += int(i.rstrip("\n").lstrip("addx "))
for i in screen:
    print("".join(i))