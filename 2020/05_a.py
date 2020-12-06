lines = [line.strip() for line in open("2020/05_input.txt", "r").readlines()]

print(max(int("".join("1" if c in ["R", "B"] else "0" for c in s), 2) for s in lines))
