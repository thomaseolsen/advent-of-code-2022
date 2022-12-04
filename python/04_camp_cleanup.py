import time

with open("../input_data/04_camp_cleanup.txt") as f:
    SECTION_LIST = f.read().split("\n")

p1_count = 0
p2_count = 0

tic1 = time.perf_counter()
for sections in SECTION_LIST:
    sect_a = sections.split(",")[0].split("-")
    sect_b = sections.split(",")[1].split("-")

    if sect_a == sect_b:
        p1_count += 1
    elif (int(sect_a[1]) - int(sect_a[0])) > (int(sect_b[1]) - int(sect_b[0])):
        # sect_a is the longer range
        if int(sect_a[1]) >= int(sect_b[1]) and int(sect_a[0]) <= int(sect_b[0]):
            p1_count += 1
    else:
        # sect_b is the larger range
        if int(sect_b[1]) >= int(sect_a[1]) and int(sect_b[0]) <= int(sect_a[0]):
            p1_count += 1
toc1 = time.perf_counter()

tic2 = time.perf_counter()
for sections in SECTION_LIST:
    sect_a = sections.split(",")[0].split("-")
    sect_b = sections.split(",")[1].split("-")

    if sect_a == sect_b:
        p2_count += 1
    elif int(sect_a[1]) >= int(sect_b[0]) and int(sect_a[0]) <= int(sect_b[0]):
        p2_count += 1
    elif int(sect_a[1]) >= int(sect_b[1]) and int(sect_a[0]) <= int(sect_b[1]):
        p2_count += 1
    elif int(sect_b[1]) >= int(sect_a[0]) and int(sect_b[0]) <= int(sect_a[0]):
        p2_count += 1
    elif int(sect_b[1]) >= int(sect_a[1]) and int(sect_b[0]) <= int(sect_a[1]):
        p2_count += 1
toc2 = time.perf_counter()

print(f"{p1_count=} in {toc1 - tic1:0.5f} seconds")  # 560
print(f"{p2_count=} in {toc2 - tic2:0.5f} seconds")  # 839
