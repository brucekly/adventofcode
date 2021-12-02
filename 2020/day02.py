import re

def letters_matching(string, target):
    n = 0
    for letter in string:
        if letter == target:
            n += 1
    return n

def parse_password(password):
    return re.split(": | |-", password)

def part1(passwords):
    n = 0
    for password in passwords:
        p = parse_password(password)
        matching = letters_matching(p[3], p[2])
        if matching >= int(p[0]) and matching <= int(p[1]):
            n += 1
    return n

def part2(passwords):
    n = 0
    for password in passwords:
        p = parse_password(password)
        matching = letters_matching(p[3], p[2])
        if (p[3][int(p[0]) - 1] == p[2]) != (p[3][int(p[1]) - 1] == p[2]):
            n += 1
    return n

if __name__ == "__main__":
    passwords = [row for row in open("./input/day02.txt")]
    print(part1(passwords), part2(passwords))
