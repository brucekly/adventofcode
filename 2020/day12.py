def move_ship(x, y, rot, inst):
    action = inst[0]
    value = int(inst[1:])
    if action == "N":
        y += value
    elif action == "S":
        y -= value
    elif action == "E":
        x += value
    elif action == "W":
        x -= value
    elif action == "L":
        rot = (rot + (value // 90)) % 4
    elif action == "R":
        rot = (rot - (value // 90)) % 4
    elif action == "F":
        if rot == 0:
            x += value
        elif rot == 1:
            y += value
        elif rot == 2:
            x -= value
        elif rot == 3:
            y -= value
    return x, y, rot

def move_waypoint(sx, sy, wx, wy, inst):
    action = inst[0]
    value = int(inst[1:])
    if action == "N":
        wy += value
    elif action == "S":
        wy -= value
    elif action == "E":
        wx += value
    elif action == "W":
        wx -= value
    elif action == "L":
        for i in range(value // 90):
            oldx = wx
            wx = -wy
            wy = oldx
    elif action == "R":
        for i in range(value // 90):
            oldy = wy
            wy = -wx
            wx = oldy
    elif action == "F":
        sx += wx * value
        sy += wy * value
    return sx, sy, wx, wy

def part1(insts):
    x = 0
    y = 0
    rot = 0
    for inst in insts:
        x, y, rot = move_ship(x, y, rot, inst)
    return abs(x) + abs(y)

def part2(insts):
    sx = 0
    sy = 0
    wx = 10
    wy = 1
    for inst in insts:
        sx, sy, wx, wy = move_waypoint(sx, sy, wx, wy, inst)
    return abs(sx) + abs(sy)

if __name__ == "__main__":
    insts = [row for row in open("./input/day12.txt")]
    print(part1(insts), part2(insts))
