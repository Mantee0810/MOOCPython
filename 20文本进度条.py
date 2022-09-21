import time

row_num = 7
print('开始执行'.center(14,'-'))
start = time.perf_counter()
for i in range(row_num+1):
    real_done = '*' * i
    real_doing = '.' * (row_num-i)
    real_rate = i/row_num

    full_row = row_num**2
    show_rate = real_rate**2
    show_done = '*' * (i**2)
    show_doing = '.' * (full_row-(i**2))

    use_time = time.perf_counter() - start
    print("\r{:^8.2%}[{}->{}]  {:.2f}s".format(show_rate,show_done,show_doing,use_time),end='')
    time.sleep(1)

print('\n'+'结束执行'.center(14,'-'))