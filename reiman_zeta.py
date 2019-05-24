import math
import time

num_1 = 1000
out = 0
i = 1
time_1 = time.time()
while i < num_1:
    out = out + (1 / i ** 2)
    i += 1
time_2 = time.time()
print(math.sqrt(out * 6), '\n')
print(math.pi)
print('the time :', time_2 - time_1)
