def aoc_01(f: str) -> tuple[int, int]:
    m = [int(line.strip()) for line in open(f).readlines()]

    def a(m: list[int]) -> int:
        return sum(m[i - 1] < m[i] for i in range(1, len(m)))

    def b(m: list[int]) -> int:
        return sum(m[i - 3] < m[i] for i in range(1, len(m)))

    return a(m), b(m)


# assert aoc_01("2021/01_sample.txt") == (7, 5)
# assert aoc_01("2021/01_input.txt") == (1548, 1589)


def aoc_02(f: str) -> tuple[int, int]:
    instructions = [(i, int(u)) for i, u in [line.strip().split(" ") for line in open(f).readlines()]]

    def a(instructions: list[tuple[str, int]]) -> int:
        h = d = 0

        # for i, u in instructions:
        #    match i:
        #        case "forward": h += u
        #        case "down": d += u
        #        case "up": d -= u

        return h * d

    def b(instructions: list[tuple[str, int]]) -> int:
        h = d = a = 0

        # for i, u in instructions:
        #    match i:
        #        case "forward":
        #            h += u
        #            d += a * u
        #        case "down": a += u
        #        case "up": a -= u

        return h * d

    return a(instructions), b(instructions)


# assert aoc_02("2021/02_sample.txt") == (150, 900)
# assert aoc_02("2021/02_input.txt") == (1924923, 1982495697)


def aoc_03(f: str) -> tuple[int, int]:
    from typing import Literal

    bits = [line.strip() for line in open(f).readlines()]

    def _most_common(bits: list[str], i) -> Literal["1", "0"]:
        cnt = sum(b[i] == "1" for b in bits)
        return "1" if cnt >= len(bits) / 2 else "0"

    def a(bits: list[str]) -> int:
        r = "".join([_most_common(bits, i) for i in range(len(bits[0]))])
        return int(r, 2) * int(r.translate(str.maketrans("01", "10")), 2)

    def b(bits: list[str]) -> int:
        bits2 = bits.copy()

        for i in range(len(bits[0])):
            if len(bits) > 1:
                bits = [b for b in bits if b[i] == _most_common(bits, i)]

            if len(bits2) > 1:
                bits2 = [b for b in bits2 if b[i] != _most_common(bits2, i)]

        return int(bits[0], 2) * int(bits2[0], 2)

    return a(bits), b(bits)


# assert aoc_03("2021/03_sample.txt") == (198, 230)
# assert aoc_03("2021/03_input.txt") == (2583164, 2784375)


def aoc_04(f: str) -> tuple[int, int]:
    from typing import Union

    with open(f) as of:
        order = [int(n) for n in of.readline().strip().split(",")]

        boards_int = [[[int(n), False] for n in l.strip().split(" ") if n != ""] for l in of.readlines() if l != "\n"]
        boards = [boards_int[i : i + 5] for i in range(0, len(boards_int), 5)]

    def a(order: list[int], boards: list[list[list[list[Union[int, bool]]]]]) -> int:
        for o in order:
            [n.__setitem__(1, True) for board in boards for line in board for n in line if o == n[0]]

            for board, board_t in zip(boards, [list(map(list, zip(*board))) for board in boards]):
                for line, col in zip(board, board_t):
                    if all([n[1] for n in line]) or all([n[1] for n in col]):
                        return o * sum([n[0] for line in board for n in line if not n[1]])
        return 0

    def b(order: list[int], boards: list[list[list[list[Union[int, bool]]]]]) -> int:
        boardswon = set()
        win = 0

        for o in order:
            [n.__setitem__(1, True) for board in boards for line in board for n in line if o == n[0]]

            i = 0
            for board, board_t in zip(boards, [list(map(list, zip(*board))) for board in boards]):
                for line, col in zip(board, board_t):
                    if all([n[1] for n in line]) or all([n[1] for n in col]):
                        win = o * sum([n[0] for line in board for n in line if not n[1]])
                        boardswon.add(i)
                        break
                i += 1
                if len(boardswon) == len(boards):
                    return win

        return win

    return a(order, boards), b(order, boards)


# assert aoc_04("2021/04_sample.txt") == (4512, 1924)
# assert aoc_04("2021/04_input.txt") == (50008, 17408)


def aoc_05(f: str) -> tuple[int, int]:
    from collections import defaultdict

    lines = [
        ((int(x1), int(y1)), (int(x2), int(y2)))
        for x1, y1, x2, y2 in [line.strip().replace(" -> ", ",").split(",") for line in open(f).readlines()]
    ]

    def a(lines: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
        plane = defaultdict[tuple[int, int], int](int)

        for (x1, y1), (x2, y2) in lines:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    plane[(y, x1)] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    plane[(y1, x)] += 1

        return sum(1 for n in plane.values() if n > 1)

    def b(lines: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
        plane = defaultdict[tuple[int, int], int](int)

        for (x1, y1), (x2, y2) in lines:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    plane[(y, x1)] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    plane[(y1, x)] += 1
            else:
                if x1 > x2:
                    x1, x2, y1, y2 = x2, x1, y2, y1
                for x in range(x1, x2 + 1):
                    if y2 > y1:
                        y = y1 + (x - x1)
                    else:
                        y = y1 - (x - x1)
                    plane[(y, x)] += 1

        return sum(1 for n in plane.values() if n > 1)

    return a(lines), b(lines)


# assert aoc_05("2021/05_sample.txt") == (5, 12)
# assert aoc_05("2021/05_input.txt") == (6564, 19172)


def aoc_06(f: str) -> tuple[int, int]:
    ages = list(map(int, open(f).read().split(",")))

    def solve(ages: list[int], days: int):
        counts = [0] * 9
        for x in ages:
            counts[x] += 1

        for _ in range(days):
            new_count = counts.pop(0)
            counts[6] += new_count
            counts.append(new_count)

        return sum(counts)

    return solve(ages, 80), solve(ages, 256)


# assert aoc_06("2021/06_sample.txt") == (5934, 26984457539)
# assert aoc_06("2021/06_input.txt") == (386640, 1733403626279)


def aoc_07(f: str) -> tuple[int, int]:
    from statistics import mean, median

    positions = list(map(int, open(f).read().split(",")))

    def a(positions: list[int]) -> int:
        m = median(positions)
        return sum([abs(p - m) for p in positions])

    def b(positions: list[int]) -> int:
        m = mean(positions)
        m1, m2 = round(m - 0.5), round(m + 0.5)
        return min(
            sum([int(0.5 * abs(p - m1) * (abs(p - m1) + 1)) for p in positions]),
            sum([int(0.5 * abs(p - m2) * (abs(p - m2) + 1)) for p in positions]),
        )

    return a(positions), b(positions)


# assert aoc_07("2021/07_sample.txt") == (37, 168)
# assert aoc_07("2021/07_input.txt") == (352997, 101571302)


def aoc_08(f: str) -> tuple[int, int]:
    entries = [
        ([set(x) for x in a.strip().split(" ")], b.strip().split(" "))
        for a, b in [line.strip().split("|") for line in open(f).readlines()]
    ]

    def a(entries: list[tuple[list[set[str]], list[str]]]):
        return sum(sum(len(digit) in [2, 3, 4, 7] for digit in output) for _, output in entries)

    def b(entries: list[tuple[list[set[str]], list[str]]]):
        r = 0
        values = {
            "abcefg": "0",
            "cf": "1",
            "acdeg": "2",
            "acdfg": "3",
            "bcdf": "4",
            "abdfg": "5",
            "abdefg": "6",
            "acf": "7",
            "abcdefg": "8",
            "abcdfg": "9",
        }

        for patterns, outputs in entries:
            mapping = {
                "a": set(["a", "b", "c", "d", "e", "f", "g"]),
                "b": set(["a", "b", "c", "d", "e", "f", "g"]),
                "c": set(["a", "b", "c", "d", "e", "f", "g"]),
                "d": set(["a", "b", "c", "d", "e", "f", "g"]),
                "e": set(["a", "b", "c", "d", "e", "f", "g"]),
                "f": set(["a", "b", "c", "d", "e", "f", "g"]),
                "g": set(["a", "b", "c", "d", "e", "f", "g"]),
            }

            for pattern in patterns:
                if len(pattern) == 2:  # 1
                    for x in ["c", "f"]:
                        mapping[x] &= pattern
                    for x in ["a", "b", "d", "e", "g"]:
                        mapping[x] -= pattern
                elif len(pattern) == 3:  # 7
                    for x in ["a", "c", "f"]:
                        mapping[x] &= pattern
                    for x in ["b", "d", "e", "g"]:
                        mapping[x] -= pattern
                elif len(pattern) == 4:  # 4
                    for x in ["b", "c", "d", "f"]:
                        mapping[x] &= pattern
                    for x in ["a", "e", "g"]:
                        mapping[x] -= pattern
                elif len(pattern) == 5:  # 2, 3, 5
                    for x in ["a", "d", "g"]:
                        mapping[x] &= pattern
                elif len(pattern) == 6:  # 0, 6, 9
                    for x in ["a", "b", "f", "g"]:
                        mapping[x] &= pattern

            for l, p in mapping.items():
                if len(p) >= 2:
                    p.difference_update(*[v for k, v in mapping.items() if k != l])

            new_mapping = {"".join(sorted(next(iter(mapping[x])) for x in k)): v for k, v in values.items()}

            r += int("".join(map(lambda x: new_mapping["".join(sorted(x))], outputs)))

        return r

    return a(entries), b(entries)


# assert aoc_08("2021/08_sample.txt") == (26, 61229)
# assert aoc_08("2021/08_input.txt") == (525, 1083859)


def aoc_09(f: str) -> tuple[int, int]:
    from typing import Tuple

    heightmap = [list(map(int, line.strip())) for line in open(f).readlines()]

    def a(heightmap: list[list[int]]) -> int:
        return sum(
            heightmap[y][x] + 1
            for y in range(len(heightmap))
            for x in range(len(heightmap[y]))
            if heightmap[y][x]
            < min(
                a
                for a in [
                    heightmap[y][x - 1] if x > 0 else None,
                    heightmap[y][x + 1] if x < len(heightmap[y]) - 1 else None,
                    heightmap[y - 1][x] if y > 0 else None,
                    heightmap[y + 1][x] if y < len(heightmap) - 1 else None,
                ]
                if a is not None
            )
        )

    def b(heightmap: list[list[int]]) -> int:
        def visit(y: int, x: int) -> set[Tuple[int, int]]:
            basin = set[Tuple[int, int]]()

            q = [(y, x)]
            while q:
                i, j = q.pop()
                if heightmap[i][j] == 9:
                    continue

                basin.add((i, j))

                q.extend(
                    [
                        l
                        for l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                        if 0 <= l[0] < len(heightmap) and 0 <= l[1] < len(heightmap[i]) and l not in basin
                    ]
                )

            return basin

        basin_sizes = list[int]()
        visited = set[Tuple[int, int]]()
        for y in range(len(heightmap)):
            for x in range(len(heightmap[y])):
                if (y, x) not in visited and (basin := visit(y, x)):
                    basin_sizes.append(len(basin))
                    visited.update(basin)

        *_, b1, b2, b3 = sorted(basin_sizes)
        return b1 * b2 * b3

    return a(heightmap), b(heightmap)


assert aoc_09("2021/09_sample.txt") == (15, 1134)
assert aoc_09("2021/09_input.txt") == (603, 786780)
