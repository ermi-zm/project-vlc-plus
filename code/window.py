# 标准库
import time
import tkinter as tk
from tkinter import ttk
import player

class CreateWindows(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_minsize(1000, 650)
        self.title('多画面播放器')


        self.frame_root = tk.Frame(self, borderwidth=0, bg='green')  # 创建添加布局主容器
        # 初始化容器
        self.playerlist=[None]*9
        self.framelist=[None]*9

        self.frame_root.rowconfigure(0, weight=1)
        self.frame_root.rowconfigure(1, weight=1)
        self.frame_root.rowconfigure(2, weight=1)
        self.frame_root.columnconfigure(0, weight=1)
        self.frame_root.columnconfigure(1, weight=1)
        self.frame_root.columnconfigure(2, weight=1)

        for key in range(9):
            self.framelist[key] = tk.Frame(self.frame_root, bg='red')
            self.framelist[key].rowconfigure(0, weight=1)
            self.framelist[key].columnconfigure(0, weight=1)
            self.framelist[key].grid(row=key//3, column=key%3, sticky="nswe",padx=5, pady=5, )


        self.frame_root.pack(expand='yes', fill='both')

    def transmit_player(self,list):

        self.playerlist = list


    def create_video_view(self):
        for key in range(9):
            self.playerlist[key].set_window(self.framelist[key].winfo_id())

