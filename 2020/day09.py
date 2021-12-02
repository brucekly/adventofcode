import itertools as it

def is_sum(target, numbers):
    for j, k in it.combinations(numbers, 2):
        if j != k and j + k == target:
            return True
    return False

def part1(numbers):
    for i, number in enumerate(numbers[25:], 25):
        if not is_sum(number, numbers[i-25:i]):
            return number

def part2(numbers):
    invalid = part1(numbers)
    for i in range(len(numbers)):
        n = 0
        target_set = []
        while sum(target_set) <= invalid:
            target_set = numbers[i:i+n]
            if sum(target_set) == invalid:
                return min(target_set) + max(target_set)
            n += 1

if __name__ == "__main__":
    numbers = [int(row) for row in open("./input/day09.txt")]
    print(part1(numbers), part2(numbers))
