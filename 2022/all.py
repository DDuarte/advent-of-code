def aoc_01(f: str) -> tuple[int, int]:
    lines = open(f).readlines() + [""]

    def a(lines: list[str]) -> int:
        highest = 0
        curr = 0
        for line in lines:
            line = line.strip()
            if line == "":
                if curr > highest:
                    highest = curr
                curr = 0
            else:
                curr += int(line)

        return highest

    def b(lines: list[str]) -> int:
        sums = []
        curr = 0
        for line in lines:
            line = line.strip()
            if line == "":
                sums.append(curr)
                curr = 0
            else:
                curr += int(line)

        sums.sort()
        return sums[-3] + sums[-2] + sums[-1]

    return a(lines), b(lines)


assert aoc_01("2022/01_sample.txt") == (24000, 45000)
assert aoc_01("2022/01_input.txt") == (69528, 206152)


def aoc_02(f: str) -> tuple[int, int]:
    from typing import Literal

    strategy = [(x, y) for x, y in [line.strip().split(" ") for line in open(f)]]
    LOST = 0
    DRAW = 3
    WIN = 6
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def a(strategy: list[tuple[str, str]]) -> int:
        def score(strat) -> int:
            match strat:
                case ("A", "Y"):
                    return PAPER + WIN
                case ("A", "X"):
                    return ROCK + DRAW
                case ("A", "Z"):
                    return SCISSORS + LOST
                case ("B", "Y"):
                    return PAPER + DRAW
                case ("B", "X"):
                    return ROCK + LOST
                case ("B", "Z"):
                    return SCISSORS + WIN
                case ("C", "Z"):
                    return SCISSORS + DRAW
                case ("C", "X"):
                    return ROCK + WIN
                case ("C", "Y"):
                    return PAPER + LOST
                case _:
                    raise UnboundLocalError

        return sum(map(score, strategy))

    def b(strategy: list[tuple[str, str]]) -> int:
        def score(strat) -> int:
            match strat:
                case ("A", "X"):
                    return LOST + SCISSORS
                case ("A", "Y"):
                    return DRAW + ROCK
                case ("A", "Z"):
                    return WIN + PAPER
                case ("B", "X"):
                    return LOST + ROCK
                case ("B", "Y"):
                    return DRAW + PAPER
                case ("B", "Z"):
                    return WIN + SCISSORS
                case ("C", "X"):
                    return LOST + PAPER
                case ("C", "Y"):
                    return DRAW + SCISSORS
                case ("C", "Z"):
                    return WIN + ROCK
                case _:
                    raise UnboundLocalError

        return sum(map(score, strategy))

    return a(strategy), b(strategy)


assert aoc_02("2022/02_sample.txt") == (15, 12)
assert aoc_02("2022/02_input.txt") == (10816, 11657)
