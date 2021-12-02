# 01A

m = [int(line.strip()) for line in open("2021/01_input.txt").readlines()]
result = sum(i > 0 and m[i - 1] < m[i] for i in range(len(m)))

assert result == 1548

print("01A:", result)

# 01B

m = [sum(g) for g in [m[i : i + 3] for i in range(len(m) - 3 + 1)]]
result = sum(i > 0 and m[i - 1] < m[i] for i in range(len(m)))

assert result == 1589

print("01B:", result)
