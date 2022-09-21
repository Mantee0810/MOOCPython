#
# 工作日模式下(上升未知，下降0.01)
# 努力到什么水平
# 才与每天1%有相同效果

# 方法1
# weekday = 0
# weekend = 0
# for i in range(365):
#     if i%7 in [0,1,2,3,4]:
#         weekday += 1
#     else:
#         weekend += 1
# power_base = pow(1.01,365)
#
# factor = (power_base/(0.99**weekend))**(1/weekday)-1
#
# print(factor)

# 方法2

def Year_Power(dayfactor):
    power = 1
    for i in range(365):
        if i % 7 in [1,2,3,4,5]:
            power *= 1+dayfactor
        else:
            power *= 1-0.01
    return power

power_base = pow(1.01,365)

dayfactor = 0.01
b_power = 1
while b_power<power_base:
    dayfactor += 0.0005
    b_power = Year_Power(dayfactor)
print(dayfactor)










