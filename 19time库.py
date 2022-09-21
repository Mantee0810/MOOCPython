import time

# 返回一个时间戳（不好用）
print(time.time())

# 返回一个可读时间，字符串形式
print(time.ctime())

# 返回一个计算机程序可处理的形式
print(time.gmtime())

# 格式化表示
t1 = time.gmtime()
print(time.strftime('%Y',t1))
t2 = '2022-08-10'
print(time.strptime(t2,'%Y-%m-%d'))

# 计时和睡眠
start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print(end-start)