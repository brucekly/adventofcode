def part1(groups):
    sum = 0
    for group in groups:
        sum += len(set(group.replace("\n", "")))
    return sum

def part2(groups):
    sum = 0
    for group in groups:
        people = map(set, group.strip().split("\n"))
        sum += len(set.intersection(*people))
    return sum

if __name__ == "__main__":
    with open("./input/day06.txt") as f:
        groups = f.read().split("\n\n")
    print(part1(groups), part2(groups))
