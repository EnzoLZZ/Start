# @Author : asta
# @Python 3.9
# @Time : 2022/5/10 21:02
# @Email : xautliuzhengzheng@163.com
from tkinter import *


class Calculator:
    def __init__(self):  # 初始化GUI界面
        self.frame = Tk()  # 创建窗口
        self.frame.title("计算圆的周长和面积")  # 添加窗体标题
        self.frame.geometry("600x300")  # 窗体大小
        self.frame.resizable(0, 0)  # 不改变窗体大小{外类型:(int, int)可能的类型:(None, None)(bool, bool)}
        self.frame["bg"] = "lightgray"  # 窗体颜色
        self.Label_input = Label(self.frame, text="请输入圆的半径：", bg="lightgray",
                                 fg="black", font=("宋体", 18, "bold"))
        self.Label_input.place(x=30, y=50)  # 标签及位置
        self.var_radius = StringVar()  # 引入一个半径变量
        self.Entry_input = Entry(self.frame, textvariable=self.var_radius, font=("宋体", 18, "bold"), width=20)
        self.Entry_input.place(x=220, y=52)  # 文本框及位置
        self.Button_cal = Button(self.frame, text="计算", font=("宋体", 18, "bold"), width=6, command=self.get_result)
        self.Button_cal.place(x=485, y=47)  # 计算按钮及位置
        self.Label_perimeter = Label(self.frame, text="圆的周长：", bg="lightgray",
                                     fg="blue", font=("宋体", 18, "bold"))
        self.Label_perimeter.place(x=105, y=110)  # 圆的周长标签及位置
        self.Label_perimeter_result = Label(self.frame, text="圆的周长的结果", bg="lightgray",
                                            fg="green", font=("宋体", 18, "bold"))
        self.Label_perimeter_result.place(x=250, y=112)  # 圆的周长结果及位置
        self.Label_area = Label(self.frame, text="圆的面积：", bg="lightgray",
                                fg="blue", font=("宋体", 18, "bold"))
        self.Label_area.place(x=105, y=160)  # 圆的面积标签及位置
        self.Label_area_result = Label(self.frame, text="圆的面积的结果", bg="lightgray",
                                       fg="green", font=("宋体", 18, "bold"))
        self.Label_area_result.place(x=250, y=162)  # 圆的面积结果及位置

        self.Label_name = Label(self.frame, text="Sweet", bg="lightgray",
                                fg="red", font=("Times New roman", 40, "bold"))
        self.Label_name.place(x=250, y=220)  # 加油

    def show(self):  # 展示窗体
        self.frame.mainloop()

    def get_result(self):
        radius = float(self.var_radius.get())
        pi = 3.1415926
        self.Label_perimeter_result["text"] = ("%.3f" % (2 * pi * radius))
        self.Label_area_result["text"] = ("%.3f" % (pi * radius * radius))  # 计算结果并展示


if __name__ == "__main__":  # 主函数
    this_GUI = Calculator()  # 根据类实例化一个对象
    this_GUI.show()  # 展示窗体
