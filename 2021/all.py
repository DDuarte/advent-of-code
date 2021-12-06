from typing import Literal, Tuple, Union


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
    with open(f) as of:
        order = [int(n) for n in of.readline().strip().split(",")]

        boards = [[[int(n), False] for n in l.strip().split(" ") if n != ""] for l in of.readlines() if l != "\n"]
        boards = [boards[i : i + 5] for i in range(0, len(boards), 5)]

    def a(order: list[int], boards: list[list[list[list[Union[int, bool]]]]]) -> int:
        for o in order:
            [n.__setitem__(1, True) for board in boards for line in board for n in line if o == n[0]]

            for board, board_t in zip(boards, [list(map(list, zip(*board))) for board in boards]):
                for line, col in zip(board, board_t):
                    if all([n[1] for n in line]) or all([n[1] for n in col]):
                        return o * sum([n[0] for line in board for n in line if not n[1]])

    def b(order: list[int], boards: list[list[list[Tuple[int, bool]]]]) -> int:
        boardswon = set()
        win = None

        for o in order:
            [n.__setitem__(1, True) for board in boards for line in board for n in line if o == n[0]]

            i = 0
            for board, boardT in zip(boards, [list(map(list, zip(*board))) for board in boards]):
                for line, col in zip(board, boardT):
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
    lines = [
        ((int(x1), int(y1)), (int(x2), int(y2)))
        for x1, y1, x2, y2 in [line.strip().replace(" -> ", ",").split(",") for line in open(f).readlines()]
    ]

    def a(lines: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
        xmax = max(max(l[0][0], l[1][0]) for l in lines) + 1
        ymax = max(max(l[0][1], l[1][1]) for l in lines) + 1

        plane = [[0 for _ in range(xmax)] for _ in range(ymax)]

        for line in lines:
            (x1, y1), (x2, y2) = line

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    plane[y][x1] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    plane[y1][x] += 1

        return sum(1 for line in plane for n in line if n > 1)

    def b(lines: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
        xmax = max(max(l[0][0], l[1][0]) for l in lines) + 1
        ymax = max(max(l[0][1], l[1][1]) for l in lines) + 1

        plane = [[0 for _ in range(xmax)] for _ in range(ymax)]
        for line in lines:
            (x1, y1), (x2, y2) = line

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    plane[y][x1] += 1
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    plane[y1][x] += 1
            else:
                if x1 > x2:
                    x1, x2, y1, y2 = x2, x1, y2, y1
                for x in range(x1, x2 + 1):
                    if y2 > y1:
                        y = y1 + (x - x1)
                    else:
                        y = y1 - (x - x1)
                    plane[y][x] += 1

        return sum(1 for line in plane for n in line if n > 1)

    return a(lines), b(lines)


assert aoc_05("2021/05_sample.txt") == (5, 12)
assert aoc_05("2021/05_input.txt") == (6564, 19172)
