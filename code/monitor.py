from PIL import ImageGrab  # 注意一定是大写
import public_value
import time


def check_color(window):
    time.sleep(1)
    im = ImageGrab.grab((window.winfo_rootx(), window.winfo_rooty(), window.winfo_rootx() + window.winfo_width(),
                         window.winfo_rooty() + window.winfo_height()))
    kd = window.winfo_width()
    gd = window.winfo_height()

    a = int(public_value.CONSTANT.PALYER_NUM ** 0.5) * 4
    port_color_xy = [None] * 9
    port_color_all = [None] * public_value.CONSTANT.PALYER_NUM

    for key in range(public_value.CONSTANT.PALYER_NUM):
        for num in range(9):
            port_color_xy[num] = im.getpixel((
                (1 / a * (num % 3 + 1) + key % (a / 4) / (a / 4))*kd , ((1 / a * (num // 3 + 1)) + key // (a / 4) / (a / 4))*gd))

        port_color_all[key] = list(port_color_xy)



    for mark in range(public_value.CONSTANT.PALYER_NUM):

        if len(set(port_color_all[mark])) < 2:
            public_value.VARIABLE.COLOUR_LSIT[mark] = "黑场故障"

        elif len(set(port_color_all[mark][0:9:3])) < 3and len(set(port_color_all[mark][1:9:3])) < 3 and len(set(port_color_all[mark][2:9:3])) < 3 :
            public_value.VARIABLE.COLOUR_LSIT[mark]="彩条故障"

        else:
            public_value.VARIABLE.COLOUR_LSIT[mark] = "播出正常"



