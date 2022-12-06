import time

with open("../input_data/06_tuning_trouble.txt") as f:
    STREAM = [*f.read()]


signal = ""
signal_location = 0

tic = time.perf_counter()
for i in range(len(STREAM)-1):
    for j in range(i, i+4):
        if STREAM[j] not in signal:
            signal += STREAM[j]
        else:
            signal = ""
            break

    if len(signal) == 4:
        signal_location = i+4
        break
toc = time.perf_counter()
print(f"{signal=} at {signal_location=} in {toc - tic:0.5f} seconds")  # 'nqsg' at 1816

tic = time.perf_counter()
for i in range(len(STREAM)-1):
    for j in range(i, i+14):
        if STREAM[j] not in signal:
            signal += STREAM[j]
        else:
            signal = ""
            break

    if len(signal) == 14:
        signal_location = i+14
        break
toc = time.perf_counter()
print(f"{signal=} at {signal_location=} in {toc - tic:0.5f} seconds")  # 'zqrpvjdbnsmlwf' at 2625
