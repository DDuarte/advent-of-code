import math

instructions = [(line[0], int(line[1:].strip())) for line in open("2020/12_input.txt", "r").readlines()]

n = e = 0
degrees = 0

for action, val in instructions:
    if action == "N":
        n += val
    elif action == "S":
        n -= val
    elif action == "E":
        e += val
    elif action == "W":
        e -= val
    elif action == "L":
        degrees += val
    elif action == "R":
        degrees -= val
    elif action == "F":
        n += val * math.sin(degrees * math.pi / 180)
        e += val * math.cos(degrees * math.pi / 180)

    print(f"{action=} {val=} {e=} {n=} {degrees=}")

print(round(abs(n) + abs(e)))
