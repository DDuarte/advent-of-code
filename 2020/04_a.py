import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passports = [
    {p.split(":")[0]: p.split(":")[1] for p in line.replace("\n", " ").split(" ")}
    for line in re.split("\n\n", open("2020/04_input.txt", "r").read().strip())
]

print(sum(1 for p in passports if all([r in p for r in required])))
