expenses = [int(line.strip()) for line in open("2020/01_input.txt", "r").readlines()]


for i in range(len(expenses)):
    for j in range(i, len(expenses)):
        for k in range(j, len(expenses)):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(expenses[i] * expenses[j] * expenses[k])
