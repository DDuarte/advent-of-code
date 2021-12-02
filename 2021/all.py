def aoc_01() -> tuple[int, int]:
    m = [int(line.strip()) for line in open("2021/01_input.txt").readlines()]

    def a(m: list[int]) -> int:
        return sum(m[i - 1] < m[i] for i in range(1, len(m)))

    def b(m: list[int]) -> int:
        return sum(m[i - 3] < m[i] for i in range(1, len(m)))

    return a(m), b(m)

assert aoc_01() == (1548, 1589)

def aoc_02() -> tuple[int, int]:
    instructions = [(i, int(u)) for i, u in [line.strip().split(" ") for line in open("2021/02_input.txt").readlines()]]

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

assert aoc_02() == (1924923, 1982495697)
