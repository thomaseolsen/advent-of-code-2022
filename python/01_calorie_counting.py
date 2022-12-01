with open("../input_data/01_calorie_counting.txt") as f:
    CALORIE_LIST = f.read().split("\n")

def top_n_sum(lst: list[int], n: int) -> int:
    ret_sum = 0
    for x in range(n):
        ret_sum += lst[x]
    return ret_sum

elves = []
current_elf = 0
for calorie in CALORIE_LIST:
    if calorie != '':
        current_elf += int(calorie)
    else:
        elves.append(current_elf)
        current_elf = 0
    
elves.sort(reverse=True)

print(elves[0])
print(top_n_sum(elves, 3))
