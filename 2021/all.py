from typing import Literal


def aoc_01(f: str) -> tuple[int, int]:
    m = [int(line.strip()) for line in open(f).readlines()]

    def a(m: list[int]) -> int:
        return sum(m[i - 1] < m[i] for i in range(1, len(m)))

    def b(m: list[int]) -> int:
        return sum(m[i - 3] < m[i] for i in range(1, len(m)))

    return a(m), b(m)

assert aoc_01("2021/01_sample.txt") == (7, 5)
assert aoc_01("2021/01_input.txt") == (1548, 1589)

def aoc_02(f: str) -> tuple[int, int]:
    instructions = [(i, int(u)) for i, u in [line.strip().split(" ") for line in open(f).readlines()]]

    def a(instructions: list[tuple[str, int]]) -> int:
        h = d = 0

        for i, u in instructions:
            match i:
                case "forward": h += u
                case "down": d += u
                case "up": d -= u

        return h * d

    def b(instructions: list[tuple[str, int]]) -> int:
        h = d = a = 0

        for i, u in instructions:
            match i:
                case "forward":
                    h += u
                    d += a * u
                case "down": a += u
                case "up": a -= u

        return h * d

    return a(instructions), b(instructions)

assert aoc_02("2021/02_sample.txt") == (150, 900)
assert aoc_02("2021/02_input.txt") == (1924923, 1982495697)

def aoc_03(f: str) -> tuple[int, int]:
    bits = [line.strip() for line in open(f).readlines()]

    def most_common(bits: list[str], i) -> Literal["1", "0"]:
        cnt = sum(b[i] == "1" for b in bits)
        return "1" if cnt >= len(bits)/2 else "0"

    def a(bits: list[str]) -> int:
        r = "".join([most_common(bits, i) for i in range(len(bits[0]))])
        return  int(r, 2) * int(r.translate(str.maketrans("01", "10")), 2)

    def b(bits: list[str]) -> int:
        bits2 = bits.copy()

        for i in range(len(bits[0])):
            if len(bits) > 1:
                bits = [b for b in bits if b[i] == most_common(bits, i)]

            if len(bits2) > 1:
                bits2 = [b for b in bits2 if b[i] != most_common(bits2, i)]

        return int(bits[0], 2) * int(bits2[0], 2)

    return a(bits), b(bits)

assert aoc_03("2021/03_sample.txt") == (198, 230)
assert aoc_03("2021/03_input.txt") == (2583164, 2784375)
