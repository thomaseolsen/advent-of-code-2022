import time

with open("../input_data/03_rucksack_reorganization.txt") as f:
    RUCKSACK_LIST = f.read().split("\n")

LOWER_ADJUST = 96
UPPER_ADJUST = 38

p1_score = 0
p2_score = 0

tic1 = time.perf_counter()
for sack in RUCKSACK_LIST:
    comp_a = sack[:len(sack)//2]
    comp_b = sack[len(sack)//2:]
    for c in comp_a:
        if comp_b.find(c) > -1:
            if c.isupper():
                p1_score += ord(c) - UPPER_ADJUST
            else:
                p1_score += ord(c) - LOWER_ADJUST
            break
toc1 = time.perf_counter()

tic2 = time.perf_counter()
for i in range(0, len(RUCKSACK_LIST), 3):
    first_two_comp = list(set(RUCKSACK_LIST[i])&set(RUCKSACK_LIST[i+1]))
    final_comp = list(set(first_two_comp)&set(RUCKSACK_LIST[i+2]))
    badge = final_comp[0]
    if badge.isupper():
        p2_score += ord(badge) - UPPER_ADJUST
    else:
        p2_score += ord(badge) - LOWER_ADJUST
toc2 = time.perf_counter()

print(f"{p1_score=} in {toc1 - tic1:0.5f} seconds")  # 7,553
print(f"{p2_score=} in {toc2 - tic2:0.5f} seconds")  # 2,758
