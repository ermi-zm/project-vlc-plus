

from PIL import ImageGrab#注意一定是大写
import public_value
import time

def show_image(w):
    time.sleep(1)
    im=ImageGrab.grab((w.winfo_rootx(),w.winfo_rooty(),w.winfo_rootx()+w.winfo_width(),w.winfo_rooty()+w.winfo_height()))
    kd=w.winfo_width()
    gd=w.winfo_height()

    def if_black(a,b):
        if max(im.getpixel((a, b)))-min(im.getpixel((a, b))) < 10 and max(im.getpixel((a, b)))<100:
            return True
        else:
            return False

    public_value.VARIABLE.COLOUR_LSIT[0]= if_black(kd / 6, gd/6)
    public_value.VARIABLE.COLOUR_LSIT[1] =if_black(kd / 2, gd / 6)
    public_value.VARIABLE.COLOUR_LSIT[2] =if_black(kd / 6 * 5, gd / 6)
    public_value.VARIABLE.COLOUR_LSIT[3] =if_black(kd / 6, gd/2)
    public_value.VARIABLE.COLOUR_LSIT[4] =if_black(kd / 2, gd / 2)
    public_value.VARIABLE.COLOUR_LSIT[5] =if_black(kd / 6 * 5, gd / 2)
    public_value.VARIABLE.COLOUR_LSIT[6] =if_black(kd / 6, gd/6*5)
    public_value.VARIABLE.COLOUR_LSIT[7] =if_black(kd / 2, gd/6*5)
    public_value.VARIABLE.COLOUR_LSIT[8] =if_black(kd / 6*5, gd/6*5)

    print( public_value.VARIABLE.COLOUR_LSIT)

   # im.show()#显示图片