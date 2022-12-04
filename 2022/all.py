def aoc_01_a(f: str) -> int:
    highest = 0
    curr = 0
    for line in open(f).readlines() + [""]:
        line = line.strip()
        if line == "":
            if curr > highest:
                highest = curr
            curr = 0
        else:
            curr += int(line)

    return highest


def aoc_01_b(f: str) -> int:
    sums = []
    curr = 0
    for line in open(f).readlines() + [""]:
        line = line.strip()
        if line == "":
            sums.append(curr)
            curr = 0
        else:
            curr += int(line)

    sums.sort()
    return sums[-3] + sums[-2] + sums[-1]


assert aoc_01_a("2022/01_sample.txt") == 24000
assert aoc_01_a("2022/01_input.txt") == 69528
assert aoc_01_b("2022/01_sample.txt") == 45000
assert aoc_01_b("2022/01_input.txt") == 206152
