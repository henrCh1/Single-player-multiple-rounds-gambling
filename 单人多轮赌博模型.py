# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:28:09 2023

@author: 86319
"""
# 导入必要的库
import random
import matplotlib.pyplot as plt

# 定义模拟赌博游戏的函数
def gambling_game():
    # 设置初始金额
    money = 1000

    # 设置要玩的回合数
    num_rounds = 100000

    # 设置赌注金额
    bet_amount = 100

    # 设置获胜概率
    win_prob = 0.5

    # 创建一个列表来存储每轮后的金额
    money_list = [money]

    # 模拟指定轮数的赌博游戏
    for i in range(num_rounds):
        # 生成0到1之间的随机数
        rand_num = random.random()

        # 如果随机数小于获胜概率，则玩家获胜
        if rand_num < win_prob:
            # 增加玩家的金额
            money += bet_amount
        # 如果随机数大于或等于获胜概率，则玩家输了
        else:
            # 减少玩家的金额
            money -= bet_amount

        # 将当前金额添加到列表中
        money_list.append(money)

    # 返回每轮后的金额列表
    return money_list

# 使用蒙特卡罗模拟来估计赌博游戏的期望值
num_simulations = 100000
total_money = 0
for i in range(num_simulations):
    total_money += gambling_game()[-1]
expected_value = total_money / num_simulations

# 打印估计的期望值
print("赌博游戏的估计期望值为：", expected_value)

# 绘制每轮赌博后的金额列表
plt.plot(gambling_game())
plt.xlabel('回合')
plt.ylabel('金额')
plt.title('1000轮赌博后的金额')
plt.show()
