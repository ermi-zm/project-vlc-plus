import threading
import winsound
class CONSTANT:
    PALYER_NUM=4
    PALYER_LINK=["udp://@225.168.130.14:3014","udp://@225.177.130.12:3012","udp://@225.168.160.19:3019","udp://@225.168.130.16:3016","","","","","",""]

class VARIABLE:
    COLOUR_LSIT=[None]* CONSTANT.PALYER_NUM

class Voice:
    # 播放声音
    @staticmethod
    def start_warning_voice():

        process_warning = threading.Thread(target=Voice.warning_voice, name="warning")
        process_warning.start()

    # 声音进程
    @staticmethod
    def warning_voice():
        # noinspection PyBroadException
        try:
            #winsound.PlaySound('SystemQuestion', flags=1)
            winsound.PlaySound('SystemAsterisk', flags=1)
            #winsound.MessageBeep(type=-1)
        except:
            pass

