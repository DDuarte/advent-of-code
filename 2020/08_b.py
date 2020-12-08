instructions = []

for line in open("2020/08_input.txt", "r").readlines():
    op, arg = line.strip().split(" ")
    instructions.append([op, arg, 0])


def execute(inst):
    try:
        accumulator = 0
        i = 0

        while True:
            # print("i=", i, inst[i], "acc=", accumulator)

            inst[i][2] += 1
            if inst[i][2] > 1:
                # print("loop detected")
                return False, accumulator

            if inst[i][0] == "jmp":
                i += int(inst[i][1]) - 1
            elif inst[i][0] == "acc":
                accumulator += int(inst[i][1])
            elif inst[i][0] == "nop":
                pass

            i += 1

            if i >= len(inst):
                return True, accumulator
    finally:
        for i in range(len(inst)):  # reset
            inst[i][2] = 0


for i in range(len(instructions)):
    if instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
    elif instructions[i][0] == "nop":
        instructions[i][0] = "jmp"

    ok, acc = execute(instructions)

    if instructions[i][0] == "jmp":
        instructions[i][0] = "nop"
    elif instructions[i][0] == "nop":
        instructions[i][0] = "jmp"

    if ok:
        print(acc)
        break
