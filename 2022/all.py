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


def aoc_02_a(f: str) -> int:
    strategy = [(x, y) for x, y in [line.strip().split(" ") for line in open(f)]]

    def score(strat) -> int:
        match strat:
            case ("A", "Y"):
                return 2 + 6
            case ("A", "X"):
                return 1 + 3
            case ("A", "Z"):
                return 3 + 0
            case ("B", "Y"):
                return 2 + 3
            case ("B", "X"):
                return 1 + 0
            case ("B", "Z"):
                return 3 + 6
            case ("C", "Z"):
                return 3 + 3
            case ("C", "X"):
                return 1 + 6
            case ("C", "Y"):
                return 2 + 0
            case _:
                raise UnboundLocalError

    return sum(map(score, strategy))


def aoc_02_b(f: str) -> int:
    strategy = [(x, y) for x, y in [line.strip().split(" ") for line in open(f)]]

    def score(strat) -> int:
        match strat:
            case ("A", "X"):
                return 0 + 3
            case ("A", "Y"):
                return 3 + 1
            case ("A", "Z"):
                return 6 + 2
            case ("B", "X"):
                return 0 + 1
            case ("B", "Y"):
                return 3 + 2
            case ("B", "Z"):
                return 6 + 3
            case ("C", "X"):
                return 0 + 2
            case ("C", "Y"):
                return 3 + 3
            case ("C", "Z"):
                return 6 + 1
            case _:
                raise UnboundLocalError

    return sum(map(score, strategy))


assert aoc_02_a("2022/02_sample.txt") == 15
assert aoc_02_a("2022/02_input.txt") == 10816
assert aoc_02_b("2022/02_sample.txt") == 12
assert aoc_02_b("2022/02_input.txt") == 11657
