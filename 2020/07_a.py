from os import replace
import re

lines = [
    re.split(
        " contain ", line.strip().replace(" bags", "").replace(" bag", "").replace(".", "").replace("no other", "")
    )
    for line in open("2020/07_input.txt", "r").readlines()
]

colors = {}

for line in lines:
    colors[line[0]] = []
    for c in line[1:]:
        if not c:
            colors[line[0]] = None
        else:
            for s in c.split(", "):
                colors[line[0]].append(" ".join(s.split(" ")[1:]))


def find(color):
    if not colors[color]:
        return False

    b = False
    for c in colors[color]:
        if color == "shiny gold":
            return True
        b |= find(c)

    return b


cnt = 0
for color in colors:
    if color != "shiny gold" and find(color):
        cnt += 1

print(cnt)
