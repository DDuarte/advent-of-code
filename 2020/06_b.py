import re

print(
    sum(
        len(set.intersection(*[set(s) for s in line.split("\n")]))
        for line in re.split("\n\n", open("2020/06_input.txt", "r").read().strip())
    )
)
