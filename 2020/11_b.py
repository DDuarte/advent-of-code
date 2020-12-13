from typing import List


def adj(ss: List[List[str]], i: int, j: int) -> str:
    # awful, an adjancy matrix would be better...
    res = ""

    ii = 1
    while i - ii >= 0:
        if ss[i - ii][j] != ".":
            res += ss[i - ii][j]  # ↑
            break
        ii += 1

    jj = 1
    while j - jj >= 0:
        if ss[i][j - jj] != ".":
            res += ss[i][j - jj]  # ←
            break
        jj += 1

    ii = 1
    jj = 1
    while i - ii >= 0 and j - jj >= 0:
        if ss[i - ii][j - jj] != ".":
            res += ss[i - jj][j - jj]  # ↖
            break
        ii += 1
        jj += 1

    ii = 1
    while i + ii < len(ss):
        if ss[i + ii][j] != ".":
            res += ss[i + ii][j]  # ↓
            break
        ii += 1

    jj = 1
    while j + jj < len(ss[0]):
        if ss[i][j + jj] != ".":
            res += ss[i][j + jj]  # →
            break
        jj += 1

    ii = 1
    jj = 1
    while i + ii < len(ss) and j + jj < len(ss[0]):
        if ss[i + ii][j + jj] != ".":
            res += ss[i + ii][j + jj]  # ↘
            break
        ii += 1
        jj += 1

    ii = 1
    jj = 1
    while i + ii < len(ss) and j - jj >= 0:
        if ss[i + ii][j - jj] != ".":
            res += ss[i + ii][j - jj]  # ↙
            break
        ii += 1
        jj += 1

    ii = 1
    jj = 1
    while i - ii >= 0 and j + jj < len(ss[0]):
        if ss[i - ii][j + jj] != ".":
            res += ss[i - ii][j + jj]  # ↗
            break
        ii += 1
        jj += 1

    return res


seats = [list(line.strip()) for line in open("2020/11_input.txt", "r").readlines()]

import copy

while True:
    next_seats = copy.deepcopy(seats)

    changed = 0

    for i, l in enumerate(seats):
        for j, s in enumerate(l):
            if s == "L" and adj(seats, i, j).count("#") == 0:
                next_seats[i][j] = "#"
                changed += 1
            elif s == "#" and adj(seats, i, j).count("#") >= 5:
                next_seats[i][j] = "L"
                changed += 1

    if not changed:
        print(sum(line.count("#") for line in next_seats))
        break

    seats = next_seats
