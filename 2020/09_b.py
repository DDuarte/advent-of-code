numbers = [int(line.strip()) for line in open("2020/09_input.txt", "r").readlines()]

P = 25

invalid = None

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
        invalid = numbers[i]
        #print(numbers[i])
        break

curr_sum = numbers[0] 
start = 0

i = 1
while i <= len(numbers): 
    while curr_sum > invalid and start < i-1: 
        curr_sum = curr_sum - numbers[start] 
        start += 1

    if curr_sum == invalid:
        print(min(numbers[start:i-1+1]) + max(numbers[start:i-1+1]))
        break

    if i < len(numbers): 
        curr_sum = curr_sum + numbers[i] 
    i += 1
