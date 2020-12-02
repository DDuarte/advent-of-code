expenses = [int(line.strip()) for line in open("1_input.txt", "r").readlines()]


for i in range(len(expenses)):
    for j in range(i, len(expenses)):
        if expenses[i] + expenses[j] == 2020:
            print(expenses[i] * expenses[j])
