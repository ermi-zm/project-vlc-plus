from PIL import ImageGrab#注意一定是大写
import public_value
import time

def check_color(window):
    time.sleep(1)
    im=ImageGrab.grab((window.winfo_rootx(), window.winfo_rooty(), window.winfo_rootx() + window.winfo_width(), window.winfo_rooty() + window.winfo_height()))
    kd=window.winfo_width()
    gd=window.winfo_height()

    a = int(public_value.CONSTANT.PALYER_NUM ** 0.5) * 4
    port_xy = [None] * 9
    port_xy_all = [None] * public_value.CONSTANT.PALYER_NUM

    for key in range(public_value.CONSTANT.PALYER_NUM):
        for num in range(9):
            port_xy[num] =(1 / a * (num % 3 + 1) + key % (a / 4) / (a / 4), (1 / a * (num // 3 + 1)) + key // (a / 4) / (a / 4))
        print(port_xy)
        print(key)
        port_xy_all[key] = port_xy

    print(port_xy_all)

    """
      for pp in port_xy_all:
            for num in range(9):
                print(im.getpixel(pp[num]))
    """


    def if_black(a,b):
        if max(im.getpixel((a, b)))-min(im.getpixel((a, b))) < 10 and max(im.getpixel((a, b)))<100:
            return "黑场！！！"
        else:
            return "播出正常"

