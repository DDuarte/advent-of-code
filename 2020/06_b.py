import re

print(
    sum(
        len(set.intersection(*map(set, line.split("\n"))))
        for line in re.split("\n\n", open("2020/06_input.txt", "r").read().strip())
    )
)
