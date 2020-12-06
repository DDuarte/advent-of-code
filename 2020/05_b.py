lines = [line.strip() for line in open("2020/05_input.txt", "r").readlines()]

seats = set(int("".join("1" if c in ["R", "B"] else "0" for c in s), 2) for s in lines)

print(set(range(min(seats), max(seats))) - seats)
