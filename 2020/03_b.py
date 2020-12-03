lines = [line.strip() for line in open("2020/03_input.txt", "r").readlines()]

def cnt(slope_r, slope_d):
    i = 0
    j = 0
    trees = 0

    while i < len(lines):
        j = (j + slope_r) % len(lines[0])
        i += slope_d

        if i < len(lines) and lines[i][j] == "#":
            trees += 1

    return trees

print(cnt(1, 1) * cnt(3, 1) * cnt(5, 1) * cnt(7, 1) * cnt(1, 2))
