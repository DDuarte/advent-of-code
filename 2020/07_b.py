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
                ss = s.split(" ")

                colors[line[0]].append((int(ss[0]), " ".join(ss[1:])))


def find(color):
    if not colors[color]:
        return 0

    b = 0
    for pair in colors[color]:
        b += pair[0] + (pair[0] * find(pair[1]))

    return b


cnt = 0
for pair in colors["shiny gold"]:
    cnt += pair[0] + (pair[0] * find(pair[1]))

print(cnt)
