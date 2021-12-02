import itertools as it

def count_adjacent(seats, x, y, char):
    n = 0
    adjacent = [[x, y] for x, y in it.product(range(x-1, x+2), range(y-1, y+2))]
    adjacent.remove([x, y])
    adjacent = filter(
        lambda a: 0 <= a[0] < len(seats[0]) and 0 <= a[1] < len(seats),
        adjacent
    )
    for [x, y] in adjacent:
        if seats[y][x] == char:
            n += 1
    return n

def count_visible(seats, x, y, char):
    n = 0
    directions = [[i, j] for i, j in it.product(range(-1, 2), range(-1, 2))]
    directions.remove([0, 0])
    visible = []
    for [i, j] in directions:
        if x+i < 0 or x+i > len(seats[0]) - 1 or y+j < 0 or y+j > len(seats) - 1:
            continue
        # print(i, j, seats[y+j][x+i])
        if seats[y+j][x+i] != ".":
            visible.append([x+i, y+j])
        else:
            dist = 2
            hit = False
            while not hit and 0 <= x+(i*dist) < len(seats[0]) and 0 <= y+(j*dist) < len(seats):
                if seats[y+(j*dist)][x+(i*dist)] != ".":
                    visible.append([x+(i*dist), y+(j*dist)])
                    hit = True
                dist += 1
    # print(x, y, visible)
    for [x, y] in visible:
        if seats[y][x] == char:
            n += 1
    return n

def step_forward(seats, nempty, check):
    new_seats = [[""] * len(seats[0]) for i in range(len(seats))]
    for y, row in enumerate(seats):
        for x, char in enumerate(row):
            if char == "L":
                if check(seats, x, y, "#") == 0:
                    new_seats[y][x] = "#"
                else:
                    new_seats[y][x] = "L"
            elif char == "#":
                if check(seats, x, y, "#") >= nempty:
                    new_seats[y][x] = "L"
                else:
                    new_seats[y][x] = "#"
            else:
                new_seats[y][x] = char
    return new_seats

def part1(seats):
    prev_seats = seats
    new_seats = step_forward(prev_seats, 4, count_adjacent)
    while new_seats != prev_seats:
        prev_seats = new_seats
        new_seats = step_forward(prev_seats, 4, count_adjacent)
    n = 0
    for row in new_seats:
        n += row.count("#")
    return n

def part2(seats):
    prev_seats = seats
    new_seats = step_forward(prev_seats, 5, count_visible)
    while new_seats != prev_seats:
        prev_seats = new_seats
        new_seats = step_forward(prev_seats, 5, count_visible)
    n = 0
    for row in new_seats:
        n += row.count("#")
    return n

if __name__ == "__main__":
    seats = [list(row.strip()) for row in open("./input/day11.txt")]
    print(part1(seats), part2(seats))
