jolts = sorted([int(line.strip()) for line in open("2020/10_input.txt", "r").readlines()])
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

s = [0]*jolts[-1]
s.insert(0, 1)

for i in jolts[1:]:
    s[i] = s[i-1] + s[i-2] + s[i-3]

print(s[-1])
