#!python
import random
from RangeUnscrambler import unscramble

fails = 0
for i in range(1, 100000):
    a = random.randint(1, 100)
    b = random.randint(a, 250)
    # print(a, b)
    res = unscramble(a, b, percentile=False)[0]
    if "not" in res:
        fails += 1
    
print(fails)
