import decimal
import sys
import time
import torch

if len(sys.argv) != 3:
    print("Invalid max, size.")
    exit(1)

max = int(sys.argv[1])
size = int(sys.argv[2])
answers = []

accumulator_ns = 0
for i in range(max):
    x = torch.rand(size, size)
    y = torch.rand(size, size)

    start_ns = time.time_ns()
    answer = x * y
    end_ns = time.time_ns()
    accumulator_ns += end_ns - start_ns 

    answers.append(answer)


printable = decimal.Decimal(accumulator_ns) / decimal.Decimal(1_000_000_000)

print(printable)
