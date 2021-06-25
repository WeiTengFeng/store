import threading
import time
bread = 0
class chef(threading.Thread):
    chef_name = ""  # 厨师姓名
    def run(self):
        global bread
        while True:
            if bread < 500:
                bread = bread + 1
                print(self.chef_name,"做了一个面包","现有面包",bread)
                time.sleep(3)
            elif bread >= 500:
                print(self.chef_name, "休息3秒")
                time.sleep(3)
class cust(threading.Thread):
    customer_name = ""  # 顾客姓名
    def run(self):
        money = 1000
        global bread
        while True:
            if bread > 0:
                bread = bread - 1
                money = money - 2
                print(self.customer_name,"买了一个面包","剩余",bread,"个面包,剩余",money,"元")
                time.sleep(2)
                if money <= 0:
                    break
            else:
                print("没面包,等两秒")
                time.sleep(2)
p1 = chef()
p2 = chef()
p3 = chef()
p4 = cust()
p5 = cust()
p6 = cust()
p7 = cust()
p1.chef_name = "厨师一"
p2.chef_name = "厨师二"
p3.chef_name = "厨师三"
p4.customer_name = "顾客一"
p5.customer_name = "顾客二"
p6.customer_name = "顾客三"
p7.customer_name = "顾客四"
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
