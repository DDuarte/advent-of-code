from typing import List


def adj(ss: List[List[str]], i: int, j: int) -> str:
    res = ""

    if i > 0:
        res += ss[i - 1][j]

    if j > 0:
        res += ss[i][j - 1]

    if i > 0 and j > 0:
        res += ss[i - 1][j - 1]

    if i + 1 < len(ss):
        res += ss[i + 1][j]

    if j + 1 < len(ss[0]):
        res += ss[i][j + 1]

    if i + 1 < len(ss) and j + 1 < len(ss[0]):
        res += ss[i + 1][j + 1]

    if i + 1 < len(ss) and j > 0:
        res += ss[i + 1][j - 1]

    if i > 0 and j + 1 < len(ss[0]):
        res += ss[i - 1][j + 1]

    return res


seats = [list(line.strip()) for line in open("2020/11_input.txt", "r").readlines()]
# print(0)
# print("\n".join("".join(line) for line in seats))
# print()

import copy

while True:
    next_seats = copy.deepcopy(seats)

    changed = 0

    for i, l in enumerate(seats):
        for j, s in enumerate(l):
            if s == "L" and adj(seats, i, j).count("#") == 0:
                next_seats[i][j] = "#"
                changed += 1
            elif s == "#" and adj(seats, i, j).count("#") >= 4:
                next_seats[i][j] = "L"
                changed += 1

    if not changed:
        print(sum(line.count("#") for line in next_seats))
        break

    seats = next_seats
