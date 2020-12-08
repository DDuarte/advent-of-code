instructions = []

for line in open("2020/08_input.txt", "r").readlines():
    op, arg = line.strip().split(" ")
    instructions.append([op, arg, 0])

accumulator = 0
i = 0

while True:
    print("i=", i, instructions[i], "acc=", accumulator)

    instructions[i][2] += 1
    if instructions[i][2] > 1:
        break

    if instructions[i][0] == "jmp":
        i += int(instructions[i][1]) - 1
    elif instructions[i][0] == "acc":
        accumulator += int(instructions[i][1])
    elif instructions[i][0] == "nop":
        pass

    i += 1

    if i > len(instructions):
        break

print(accumulator)
