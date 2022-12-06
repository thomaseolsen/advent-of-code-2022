import re
import time

with open("../input_data/05_supply_stacks.txt") as f:
    INSTRUCTION_LIST = f.read().split("\n")

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []
moves = []

in_stacks = True
for line in INSTRUCTION_LIST:
    if line == " 1   2   3   4   5   6   7   8   9 ":
        in_stacks = False
        stack_1.reverse()
        stack_2.reverse()
        stack_3.reverse()
        stack_4.reverse()
        stack_5.reverse()
        stack_6.reverse()
        stack_7.reverse()
        stack_8.reverse()
        stack_9.reverse()
    
    if in_stacks:
        if line[1] != " ":
            stack_1.append(line[1])
        if line[5] != " ":
            stack_2.append(line[5])
        if line[9] != " ":
            stack_3.append(line[9])
        if line[13] != " ":
            stack_4.append(line[13])
        if line[17] != " ":
            stack_5.append(line[17])
        if line[21] != " ":
            stack_6.append(line[21])
        if line[25] != " ":
            stack_7.append(line[25])
        if line[29] != " ":
            stack_8.append(line[29])
        if line[33] != " ":
            stack_9.append(line[33])
    else:
        regex = re.compile("move (\d\d*) from (\d\d*) to (\d\d*)")
        groups = regex.match(line)
        if not groups:
            continue
        counter = groups.group(1)
        source = groups.group(2)
        destination = groups.group(3)
        moves.append([counter, source, destination])

tic1 = time.perf_counter()
for move in moves:
    counter = int(move[0])
    source = int(move[1])
    destination = int(move[2])

    for _ in range(counter):
        if source == 1 and destination == 2:
            stack_2.append(stack_1.pop())
        if source == 1 and destination == 3:
            stack_3.append(stack_1.pop())
        if source == 1 and destination == 4:
            stack_4.append(stack_1.pop())
        if source == 1 and destination == 5:
            stack_5.append(stack_1.pop())
        if source == 1 and destination == 6:
            stack_6.append(stack_1.pop())
        if source == 1 and destination == 7:
            stack_7.append(stack_1.pop())
        if source == 1 and destination == 8:
            stack_8.append(stack_1.pop())
        if source == 1 and destination == 9:
            stack_9.append(stack_1.pop())

        if source == 2 and destination == 1:
            stack_1.append(stack_2.pop())
        if source == 2 and destination == 3:
            stack_3.append(stack_2.pop())
        if source == 2 and destination == 4:
            stack_4.append(stack_2.pop())
        if source == 2 and destination == 5:
            stack_5.append(stack_2.pop())
        if source == 2 and destination == 6:
            stack_6.append(stack_2.pop())
        if source == 2 and destination == 7:
            stack_7.append(stack_2.pop())
        if source == 2 and destination == 8:
            stack_8.append(stack_2.pop())
        if source == 2 and destination == 9:
            stack_9.append(stack_2.pop())

        if source == 3 and destination == 2:
            stack_2.append(stack_3.pop())
        if source == 3 and destination == 1:
            stack_1.append(stack_3.pop())
        if source == 3 and destination == 4:
            stack_4.append(stack_3.pop())
        if source == 3 and destination == 5:
            stack_5.append(stack_3.pop())
        if source == 3 and destination == 6:
            stack_6.append(stack_3.pop())
        if source == 3 and destination == 7:
            stack_7.append(stack_3.pop())
        if source == 3 and destination == 8:
            stack_8.append(stack_3.pop())
        if source == 3 and destination == 9:
            stack_9.append(stack_3.pop())

        if source == 4 and destination == 2:
            stack_2.append(stack_4.pop())
        if source == 4 and destination == 3:
            stack_3.append(stack_4.pop())
        if source == 4 and destination == 1:
            stack_1.append(stack_4.pop())
        if source == 4 and destination == 5:
            stack_5.append(stack_4.pop())
        if source == 4 and destination == 6:
            stack_6.append(stack_4.pop())
        if source == 4 and destination == 7:
            stack_7.append(stack_4.pop())
        if source == 4 and destination == 8:
            stack_8.append(stack_4.pop())
        if source == 4 and destination == 9:
            stack_9.append(stack_4.pop())

        if source == 5 and destination == 2:
            stack_2.append(stack_5.pop())
        if source == 5 and destination == 3:
            stack_3.append(stack_5.pop())
        if source == 5 and destination == 4:
            stack_4.append(stack_5.pop())
        if source == 5 and destination == 1:
            stack_1.append(stack_5.pop())
        if source == 5 and destination == 6:
            stack_6.append(stack_5.pop())
        if source == 5 and destination == 7:
            stack_7.append(stack_5.pop())
        if source == 5 and destination == 8:
            stack_8.append(stack_5.pop())
        if source == 5 and destination == 9:
            stack_9.append(stack_5.pop())

        if source == 6 and destination == 2:
            stack_2.append(stack_6.pop())
        if source == 6 and destination == 3:
            stack_3.append(stack_6.pop())
        if source == 6 and destination == 4:
            stack_4.append(stack_6.pop())
        if source == 6 and destination == 5:
            stack_5.append(stack_6.pop())
        if source == 6 and destination == 1:
            stack_1.append(stack_6.pop())
        if source == 6 and destination == 7:
            stack_7.append(stack_6.pop())
        if source == 6 and destination == 8:
            stack_8.append(stack_6.pop())
        if source == 6 and destination == 9:
            stack_9.append(stack_6.pop())

        if source == 7 and destination == 2:
            stack_2.append(stack_7.pop())
        if source == 7 and destination == 3:
            stack_3.append(stack_7.pop())
        if source == 7 and destination == 4:
            stack_4.append(stack_7.pop())
        if source == 7 and destination == 5:
            stack_5.append(stack_7.pop())
        if source == 7 and destination == 6:
            stack_6.append(stack_7.pop())
        if source == 7 and destination == 1:
            stack_1.append(stack_7.pop())
        if source == 7 and destination == 8:
            stack_8.append(stack_7.pop())
        if source == 7 and destination == 9:
            stack_9.append(stack_7.pop())

        if source == 8 and destination == 2:
            stack_2.append(stack_8.pop())
        if source == 8 and destination == 3:
            stack_3.append(stack_8.pop())
        if source == 8 and destination == 4:
            stack_4.append(stack_8.pop())
        if source == 8 and destination == 5:
            stack_5.append(stack_8.pop())
        if source == 8 and destination == 6:
            stack_6.append(stack_8.pop())
        if source == 8 and destination == 7:
            stack_7.append(stack_8.pop())
        if source == 8 and destination == 1:
            stack_1.append(stack_8.pop())
        if source == 8 and destination == 9:
            stack_9.append(stack_8.pop())

        if source == 9 and destination == 2:
            stack_2.append(stack_9.pop())
        if source == 9 and destination == 3:
            stack_3.append(stack_9.pop())
        if source == 9 and destination == 4:
            stack_4.append(stack_9.pop())
        if source == 9 and destination == 5:
            stack_5.append(stack_9.pop())
        if source == 9 and destination == 6:
            stack_6.append(stack_9.pop())
        if source == 9 and destination == 7:
            stack_7.append(stack_9.pop())
        if source == 9 and destination == 8:
            stack_8.append(stack_9.pop())
        if source == 9 and destination == 1:
            stack_1.append(stack_9.pop())
toc1 = time.perf_counter()

print(f"{stack_1.pop()}{stack_2.pop()}{stack_3.pop()}{stack_4.pop()}{stack_5.pop()}{stack_6.pop()}{stack_7.pop()}{stack_8.pop()}{stack_9.pop()} in {toc1 - tic1:0.5f} seconds")  # LBLVVTVLP

stack_1 = []
stack_2 = []
stack_3 = []
stack_4 = []
stack_5 = []
stack_6 = []
stack_7 = []
stack_8 = []
stack_9 = []
moves = []

in_stacks = True
for line in INSTRUCTION_LIST:
    if line == " 1   2   3   4   5   6   7   8   9 ":
        in_stacks = False
        stack_1.reverse()
        stack_2.reverse()
        stack_3.reverse()
        stack_4.reverse()
        stack_5.reverse()
        stack_6.reverse()
        stack_7.reverse()
        stack_8.reverse()
        stack_9.reverse()
    
    if in_stacks:
        if line[1] != " ":
            stack_1.append(line[1])
        if line[5] != " ":
            stack_2.append(line[5])
        if line[9] != " ":
            stack_3.append(line[9])
        if line[13] != " ":
            stack_4.append(line[13])
        if line[17] != " ":
            stack_5.append(line[17])
        if line[21] != " ":
            stack_6.append(line[21])
        if line[25] != " ":
            stack_7.append(line[25])
        if line[29] != " ":
            stack_8.append(line[29])
        if line[33] != " ":
            stack_9.append(line[33])
    else:
        regex = re.compile("move (\d\d*) from (\d\d*) to (\d\d*)")
        groups = regex.match(line)
        if not groups:
            continue
        counter = groups.group(1)
        source = groups.group(2)
        destination = groups.group(3)
        moves.append([counter, source, destination])

tic2 = time.perf_counter()
for move in moves:
    counter = int(move[0])
    source = int(move[1])
    destination = int(move[2])
    stack = []

    for _ in range(counter):
        if source == 1:
            stack.append(stack_1.pop())
        if source == 2:
            stack.append(stack_2.pop())
        if source == 3:
            stack.append(stack_3.pop())
        if source == 4:
            stack.append(stack_4.pop())
        if source == 5:
            stack.append(stack_5.pop())
        if source == 6:
            stack.append(stack_6.pop())
        if source == 7:
            stack.append(stack_7.pop())
        if source == 8:
            stack.append(stack_8.pop())
        if source == 9:
            stack.append(stack_9.pop())
    
    stack.reverse()

    if destination == 1:
        for crate in stack:
            stack_1.append(crate)
    if destination == 2:
        for crate in stack:
            stack_2.append(crate)
    if destination == 3:
        for crate in stack:
            stack_3.append(crate)
    if destination == 4:
        for crate in stack:
            stack_4.append(crate)
    if destination == 5:
        for crate in stack:
            stack_5.append(crate)
    if destination == 6:
        for crate in stack:
            stack_6.append(crate)
    if destination == 7:
        for crate in stack:
            stack_7.append(crate)
    if destination == 8:
        for crate in stack:
            stack_8.append(crate)
    if destination == 9:
        for crate in stack:
            stack_9.append(crate)
toc2 = time.perf_counter()

print(f"{stack_1.pop()}{stack_2.pop()}{stack_3.pop()}{stack_4.pop()}{stack_5.pop()}{stack_6.pop()}{stack_7.pop()}{stack_8.pop()}{stack_9.pop()} in {toc1 - tic1:0.5f} seconds")  # TPFFBDRJD
