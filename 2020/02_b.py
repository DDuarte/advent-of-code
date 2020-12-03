lines = [line.strip().split(" ") for line in open("2020/02_input.txt", "r").readlines()]

cnt = 0

for line in lines:
    pos = line[0].split("-")
    pos1, pos2, letter, passw = int(pos[0]), int(pos[1]), line[1].rstrip(":"), line[2]

    if (passw[pos1 - 1] == letter) != (passw[pos2 - 1] == letter):
        cnt += 1

print(cnt)
