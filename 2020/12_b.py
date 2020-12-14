import math

instructions = [(line[0], int(line[1:].strip())) for line in open("2020/12_input.txt", "r").readlines()]

n = e = 0
wn = 1
we = 10

for action, val in instructions:
    if action == "N":
        wn += val
    elif action == "S":
        wn -= val
    elif action == "E":
        we += val
    elif action == "W":
        we -= val
    elif action == "L":
        cos = round(math.cos(val * math.pi / 180))
        sin = round(math.sin(val * math.pi / 180))
        wee = we
        we = wee * cos - wn * sin
        wn = wee * sin + wn * cos
    elif action == "R":
        cos = round(math.cos((-val) * math.pi / 180))
        sin = round(math.sin((-val) * math.pi / 180))
        wee = we
        we = wee * cos - wn * sin
        wn = wee * sin + wn * cos
    elif action == "F":
        n += val * wn
        e += val * we

    # print(f"{action=} {val=} {e=} {n=} {we=} {wn=}")

print(round(abs(n) + abs(e)))
