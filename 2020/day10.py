from collections import Counter

def part1(adapters):
    data = sorted(adapters) + [(max(adapters) + 3)]
    differences = {}
    prev_adapter = 0
    for adapter in data:
        d = adapter - prev_adapter
        if d in differences:
            differences[d] += 1
        else:
            differences[d] = 1
        prev_adapter = adapter
    return differences[1] * differences[3]

def part2(adapters):
    data = sorted(adapters + [0])
    c = Counter({0:1})
    for x in data:
        c[x+1] += c[x]
        c[x+2] += c[x]
        c[x+3] += c[x]
    return c[max(data) + 3]

if __name__ == "__main__":
    adapters = [int(row) for row in open("./input/day10.txt")]
    print(part1(adapters), part2(adapters))
