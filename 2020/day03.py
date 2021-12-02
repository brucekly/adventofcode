from functools import *
import operator as op

slopes = [
    [1,  1],
    [3,  1],
    [5,  1],
    [7,  1],
    [1,  2],
]

def trees(slope):
    right = slope[0]
    down = slope[1]
    n = 0
    for i, row in enumerate(rows[::down]):
        square = row[(i * right) % len(row)]
        if square == "#":
            n += 1
    return n

def part1(rows):
    return trees([3, 1])

def part2(rows):
    return reduce(op.mul, map(trees, slopes))

if __name__ == "__main__":
    rows = [row.strip() for row in open("./input/day03.txt")]
    print(part1(rows), part2(rows))
