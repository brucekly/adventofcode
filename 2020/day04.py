import re

def part1(passports):
    valid = passports.copy()
    fields = [
        re.compile(r"\bbyr:.+\b"),
        re.compile(r"\biyr:.+\b"),
        re.compile(r"\beyr:.+\b"),
        re.compile(r"\bhgt:.+\b"),
        re.compile(r"\bhcl:.+\b"),
        re.compile(r"\becl:.+\b"),
        re.compile(r"\bpid:.+\b"),
    ]
    for field in fields:
        valid = list(filter(field.search, valid))
    return len(valid)

def part2(passports):
    valid = passports.copy()
    fields = [
        re.compile(r"\bbyr:(19[2-9]\d|200[0-2])\b"),
        re.compile(r"\biyr:(201\d|2020)\b"),
        re.compile(r"\beyr:(202\d|2030)\b"),
        re.compile(r"\bhgt:(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)\b"),
        re.compile(r"\bhcl:#[0-9a-f]{6}\b"),
        re.compile(r"\becl:(amb|blu|brn|gry|grn|hzl|oth)\b"),
        re.compile(r"\bpid:\d{9}\b"),
    ]
    for field in fields:
        valid = list(filter(field.search, valid))
    return len(valid)

if __name__ == "__main__":
    with open("./input/day04.txt") as f:
        passports = f.read().replace("\n", " ").strip().split("  ")
    print(part1(passports), part2(passports))
