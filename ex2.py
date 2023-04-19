# 金融量化分析

# 附件中有一份沪深300连接基金的历史数据。数据从2009年开始记录，
# 假设你在2009年开始，每个交易日购买1块钱份额的该沪深300连接基金，
# 请计算一下到文件中最后一天截至，你投入了多少钱，你的基金现在市值多少钱？
# 假设你愿意在定投策略上做一些改进
# （比如：每天获得一块钱本金，但不急着投入市场，而是等到市场连跌i天（如5天）后将现有的本金一次投入市场），
# 请问你在文件最后一天可以拥有多少市值？欢迎大家自己写策略挑战这个市值。**严禁使用未来数据


import xlrd

file = xlrd.open_workbook("data.xls")  # 打开文件
sheet1 = file.sheets()[0]  # 打开sheet，第一个sheet用[0]表示
change = sheet1.col_values(3)  # 第4列所有的值
value = sheet1.col_values(5)  # 第6列所有的值

total = 0 # 总份额
print("投入"+'%.2f' % ((len(value)-1)*(1+0.0012))+"元")
for i in range(1, len(value)):
    total = total + (1/(value[i]))
print("现在基金市值"+'%.2f' % (total*value[-1]) + "元")

# 连续五天跌就买
count_day = 0
count_money = 0
total2 = 0
for i in range(1, len(change)):
    num = float(change[i][0:-1])
    if num < 0:
        count_day += 1
        if count_day == 5:
            total2 += (count_money+1)/(value[i])
            count_money = 0
            count_day = 0
        else:
            count_money += 1
    else:
        count_day = 0
        count_money += 1
print("策略为连跌五天就买")
print("改变策略后基金市值"+'%.2f' % (total2*value[-1]) + "元")



