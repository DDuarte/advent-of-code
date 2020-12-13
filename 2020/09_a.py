numbers = [int(line.strip()) for line in open("2020/09_input.txt", "r").readlines()]

print(numbers)

P = 25

for i in range(P, len(numbers[P:])):
    found = False

    for j in range(i - P, i):
        for k in range(j + 1, i):
            # print(i, j, k, numbers[i], numbers[j], numbers[k])
            if numbers[i] == numbers[j] + numbers[k]:
                found = True
                break

        if found:
            break

    if not found:
        print(numbers[i])
        break
