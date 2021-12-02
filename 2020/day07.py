import re

def inner_to_dict(bag):
    inner_split = re.compile("(\d+) ([a-z ]+) bags?")
    match = inner_split.search(bag)
    if match:
        return {match[2]: int(match[1])}
    else:
        return {}

def contains_bag(bags, bag, contains):
    for subbag in bags[bag]:
        if contains in subbag:
            return True
        if contains_bag(bags, subbag, contains):
            return True
    return False

def children(bags, bag):
    if bags[bag] == {}:
        return 1
    total = 1
    for subbag in bags[bag]:
        total += bags[bag][subbag] * children(bags, subbag)
    return total

def part1():
    total = 0
    for bag in bags.keys():
        if contains_bag(bags, bag, "shiny gold"):
            total += 1
    return total

def part2():
    return children(bags, "shiny gold") - 1

if __name__ == "__main__":
    rules = [row for row in open("./input/day07.txt")]
    bags = {}
    for rule in rules:
        split_outer = re.compile("([a-z ]+) bags contain (.+)")
        color = split_outer.match(rule)[1]
        inner_bags = split_outer.match(rule)[2].replace(".", "").split(", ")
        inner_bags_list = list(map(inner_to_dict, inner_bags))
        inside = {k: int(v) for d in inner_bags_list for k, v in d.items()}
        bags[color] = inside
    print(part1(), part2())
