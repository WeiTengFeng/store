'''
#   random:随机数
    1.导入随机数：import random
    2.使用这个工具里的方法randint()

范围在0~150
money为5000
猜15次
如果输入大了，温馨提示：大了
如果输入小了，温馨提示：小了
猜错一次扣500
正好猜中，恭喜您，猜中。本次猜的数字为num

'''
import  random
# 1、系统产生随机数
num = random.randint(0,15)

# 2、开始输入您要猜的数
i = 0
money = 5000
while i < 15:
    # 3、任务：输入数据并比对数据
    number = input("请输入您要猜的数")
    number = int(number) # “56”——>56
    #判断
    if number > num:
        money = money - 500
        i = i + 1
        print("大了，money扣500!剩余余额为",money)
    elif number < num:
        money = money - 500
        i = i + 1
        print("小了，money扣500!剩余余额为",money)
    else :
        money = money + 3000
        i = 0
        print("恭喜猜中，奖励3000！剩余余额为",money)
    if i == 15:
        print("次数用完，系统锁定")
        break
    elif money == 0:
        print("金币用完，系统锁定")
        break













