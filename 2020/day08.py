def part1():
    line = 0
    acc = 0
    visited = {0}
    while True:
        inst = insts[line].split()
        if inst[0] == "nop":
            line += 1
        elif inst[0] == "jmp":
            line += int(inst[1])
        elif inst[0] == "acc":
            line += 1
            acc += int(inst[1])
        if line in visited:
            return acc
        visited.add(line)

def part2():
    for i, inst in enumerate(insts):
        modinsts = insts.copy()
        if "acc" in inst:
            continue
        elif "jmp" in inst:
            modinsts[i] = inst.replace("jmp", "nop")
        elif "nop" in inst:
            modinsts[i] = inst.replace("nop", "jmp")
        line = 0
        acc = 0
        t = 0
        while 0 <= line < len(insts) and t <= len(insts):
            t += 1
            inst = modinsts[line].split()
            if inst[0] == "nop":
                line += 1
            elif inst[0] == "jmp":
                line += int(inst[1])
            elif inst[0] == "acc":
                line += 1
                acc += int(inst[1])
        if line >= len(insts) - 1:
            return acc

if __name__ == "__main__":
    insts = [inst for inst in open("./input/day08.txt")]
    print(part1(), part2())
