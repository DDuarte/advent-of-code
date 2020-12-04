import re
import string

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = [
    {p.split(":")[0]: p.split(":")[1] for p in line.replace("\n", " ").split(" ")}
    for line in re.split("\n\n", open("2020/04_input.txt", "r").read().strip())
]

cnt = 0
for p in passports:
    if not all(r in p for r in required):
        continue

    if len(p["byr"]) != 4 or int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
        continue

    if len(p["iyr"]) != 4 or int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
        continue

    if len(p["eyr"]) != 4 or int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
        continue

    if p["hgt"].endswith("cm"):
        if int(p["hgt"].replace("cm", "")) < 150 or int(p["hgt"].replace("cm", "")) > 193:
            continue
    elif p["hgt"].endswith("in"):
        if int(p["hgt"].replace("in", "")) < 59 or int(p["hgt"].replace("in", "")) > 76:
            continue
    else:
        continue

    if (
        not p["hcl"].startswith("#")
        or len(p["hcl"]) != 7
        or not all(c in string.hexdigits.lower() for c in p["hcl"][1:7])
    ):
        continue

    if p["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue

    if len(p["pid"]) != 9 or not p["pid"].isdigit():
        continue

    cnt += 1

print(cnt)
