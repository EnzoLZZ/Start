
import random
import string

count = 0
while count < 5:
    car_nums = []  # 存储用户的选择号码
    for i in range(10):
        n1 = random.choice(string.ascii_uppercase)  # 生成首字母
        n2 = "".join(random.sample(string.ascii_uppercase + string.digits, 5))
        c_num = f"京{n1}-{n2}"
        car_nums.append(c_num)  # 生成的号码添加到列表
        print(i + 1, c_num)
    choice = input("请输入你喜欢的号码:").strip()
    if choice in car_nums:
        print(f"恭喜你选择了新车号码牌：{choice}")
        exit("good luck!!!")
    else:
        print("不合法的选择")
    count += 1
