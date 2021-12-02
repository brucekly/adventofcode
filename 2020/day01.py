import itertools as it

def part1(numbers):
    for i, j in it.combinations(numbers, 2):
        if i + j == 2020:
            return i * j

def part2(numbers):
    for i, j, k in it.combinations(numbers, 3):
        if i + j + k == 2020:
            return i * j * k

if __name__ == "__main__":
    numbers = [int(row) for row in open("./input/day01.txt")]
    print(part1(numbers), part2(numbers))
