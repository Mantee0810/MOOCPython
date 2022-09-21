import random
import time


dots = 1000000

hit = 0

start_time = time.perf_counter()

for i in range(dots):
    x,y = random.random(),random.random()
    dist = pow(x,2)+pow(y,2)
    if dist<1:
        hit += 1

pi = 4*hit/dots

end_time = time.perf_counter()
use_time = end_time-start_time
print("π的估计值为{}\n计算用时为{:.6f}秒".format(pi,use_time))


