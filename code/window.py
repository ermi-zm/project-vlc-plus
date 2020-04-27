# 标准库
import time
import tkinter as tk
from tkinter import ttk
import player
import image
import public_value
class CreateWindows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_minsize(1000, 650)
        self.title('多画面播放器')

        self.state("zoomed")
        self.menu_top = CreateMenu(self)  # 创建添加菜单栏
        self.config(menu=self.menu_top)
        self.frame_root = tk.Frame(self, borderwidth=0, bg='green')  # 创建添加布局主容器
        # 初始化容器
        self.playerlist=[None]*9
        self.framelist=[None]*9
        self.lablelist=[None]*9

        self.frame_root.rowconfigure(0, weight=9)
        self.frame_root.rowconfigure(1, weight=1)
        self.frame_root.rowconfigure(2, weight=9)
        self.frame_root.rowconfigure(3, weight=1)
        self.frame_root.rowconfigure(4, weight=9)
        self.frame_root.rowconfigure(5, weight=1)

        self.frame_root.columnconfigure(0, weight=1)
        self.frame_root.columnconfigure(1, weight=1)
        self.frame_root.columnconfigure(2, weight=1)

        for key in range(9):
            self.framelist[key] = tk.Frame(self.frame_root, bg='black')
            self.framelist[key].rowconfigure(0, weight=1)
            self.framelist[key].columnconfigure(0, weight=1)

            self.lablelist[key] = tk.Label(self.frame_root, text='正常播出', bg='#a8ff78', fg='black', font=20, width=10,
                                           height=1, anchor='c')
            self.framelist[key].grid(row=(key // 3)*2, column=key % 3, sticky="nswe", padx=5)
            self.lablelist[key].grid(row=(key // 3)*2+1, column=key % 3, sticky="nswe", padx=5)




        self.frame_root.pack(expand='yes', fill='both')

    def refresh_windows(self):
        image.show_image(self)

        for num in range(len(public_value.VARIABLE.COLOUR_LSIT)):
            if public_value.VARIABLE.COLOUR_LSIT[num]:
                self.lablelist[num].configure(text="黑场！！！",bg="red")
            else:
                self.lablelist[num].configure(text="播出正常", bg="green")
                self.lablelist[num].tkraise()


        self.after(2000, lambda: self.refresh_windows())  # 进程500毫秒触发一次

    def transmit_player(self,list):

        self.playerlist = list


    def create_video_view(self):
        for key in range(9):
            self.playerlist[key].set_window(self.framelist[key].winfo_id())




class CreateMenu(tk.Menu):
    def __init__(self, master):
        tk.Menu.__init__(self, master)
        self.__menu_1 = tk.Menu(self)
        self.__menu_2 = tk.Menu(self)
        self.add_cascade(label='文件', menu=self.__menu_1)
        self.add_cascade(label='关于', menu=self.__menu_2)

        self.__menu_1.add_command(label='测试入口',command=lambda :image.show_image(master))
