import re

def find_seat(boarding_pass: str, lh: int, uh: int, bound: int) -> int:
    lower = 0
    upper = bound
    splits = re.search(f"[{lh}{uh}]+", boarding_pass)
    for s in splits[0]:
        if upper - lower == 1:
            return (lower if s == lh else upper)
        elif s == lh:
            upper -= round((upper - lower) / 2)
        elif s == uh:
            lower += round((upper - lower) / 2)
    return lower

def part1(seats: list) -> int:
    return max(seats)

def part2(seats: list) -> int:
    last_seat = seats[0]
    for seat in seats:
        if seat - last_seat > 1:
            my_seat = seat - 1
            break
        last_seat = seat
    return my_seat

if __name__ == "__main__":
    boarding_passes = [row.strip() for row in open("./input/day05.txt")]
    seats = []
    for boarding_pass in boarding_passes:
        row = find_seat(boarding_pass, "F", "B", 127)
        column = find_seat(boarding_pass, "L", "R", 7)
        seats.append(row * 8 + column)
    seats.sort()
    print(part1(seats), part2(seats))
