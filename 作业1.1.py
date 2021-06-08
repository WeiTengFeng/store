# # 实现输入10个数字，并打印10个数的求和结果
# i = 1
# sum = 0
# while i <= 10:
#     a = int(input("请输入%d个数："%i))
#     sum += a
#     i += 1
# print(sum)





# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
# i = 1  # 次数=1
# sum = 0  # 总和=0
# max = 0
# while i <= 10:
#     a = int(input("请输入%d个数:"%i))
#     i += 1
#     sum = sum+a
#     if max < a:
#         max = a
# print("最大值为：max") # 最大值为 ”max“
# print("总和:sum") # 打印总和为”sum“
# print("平均值为：int(sum/10)") # 平均值为int(sum/10)



# 使用random模块，如何产生 50~150之间的数
# import random
# num = random.randint(50,150)
# print(num)



# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# while True:
#     a = int(input("请输入一边长度:"))
#     b = int(input("请输入另一边长度:"))
#     c = int(input("请输入另一边长度:"))
#     if a+b>c and a+c>b and b+c>a:
#         print("可以构成三角形")
#     elif a == b != c and a == c != b and b == c != a:
#         print("构成等腰三角形")
#     elif a == b == c:
#         print("构成等边三角形")
#     elif a**a+b**b==c**c:
#         print("构成直角三角形")
#     else:
#         print("不能形成三角形")



# 有以下两个数，使用+，-号实现两个数的调换。
# a = 56
# b = 78
# a = b + a
# b = a - b
# a = a - b
# print(a,b)



# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# i = 1
# while i < 4:
#     name = "root"
#     password = "admin"
#     n = (input("请输入用户名："))
#     p = (input("请输入密码："))
#     if n != name or p != password:
#         i = i + 1
#         print("密码输入错误，系统锁定")



# 使用while编程实现求1~100以内的数的和！
# i=1
# sum=0
# while i < 101:
#     sum=sum+i
#     i += 1
# print(sum)



# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# j = 0
# day = 1
# while True:
#     j += 3
#     if j >= 20:
#         break
#     j -= 2
#     day += 1
# print(day)



# 有一个列表，[“北京”,”上海”,”广东”]
# 1)	将中国所有省会城市添加到上述列表中
#
#
# 2)	广东成为第二大发达城市，将广东排在上海前面
#
#
# 3)	[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
#        这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# names = ["北京","上海","广东","深圳","重庆","苏州","成都","杭州"]
# print(names)
# names[1] = "广东"
# names[2] = "上海"
# print(names)
# nums = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# nums = sum(nums)
# names = len(names)
# print("GDP总和为：%.2f"%nums)
# p = nums / names
# print("平均GDP：%.2f"%p)




# 有以下一个列表，求其中是5的倍数的和
# a = [1,5,21,30,15,9,30,24]
# b = len(a)
# c = 0
# for n in range(b):
#     if a[n]%5 == 0:
#         c += a[n]
# print(c)






