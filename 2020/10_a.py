jolts = sorted([int(line.strip()) for line in open("2020/10_input.txt", "r").readlines()])
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

diff1 = 0
diff3 = 0
i = 1

while i < len(jolts):
    d = jolts[i] - jolts[i - 1]
    if d == 1:
        diff1 += 1
    elif d == 3:
        diff3 += 1

    i += 1

print(diff1 * diff3)
