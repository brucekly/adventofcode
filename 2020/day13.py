from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part1(earliest, buses):
    bus_id = 0
    wait_time = float("inf")
    for bus in buses:
        if bus == "x":
            continue
        elif earliest % int(bus) == 0:
            return 0
        this_wait_time = (earliest // int(bus) + 1) * int(bus) - earliest
        if this_wait_time < wait_time:
            wait_time = this_wait_time
            bus_id = int(bus)
    return bus_id * wait_time

def part2(buses):
    residues = [int(bus) for bus in buses if bus != "x"]
    moduli = [-i % int(bus) for i, bus in enumerate(buses) if bus != "x"]
    return chinese_remainder(residues, moduli)

if __name__ == "__main__":
    timetable = [row for row in open("./input/day13.txt")]
    earliest = int(timetable[0])
    buses = timetable[1].split(",")
    print(part1(earliest, buses), part2(buses))
