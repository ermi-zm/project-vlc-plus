import public_value
import player


class PlayerTop:
    def __init__(self):
        self.playerlist = [None] * public_value.CONSTANT.PALYER_NUM
        for key in range(public_value.CONSTANT.PALYER_NUM):
            self.playerlist[key] = player.Player()

    def play_start(self):

        for num in range(public_value.CONSTANT.PALYER_NUM):
            self.playerlist[num].play(public_value.CONSTANT.PALYER_LINK[num])