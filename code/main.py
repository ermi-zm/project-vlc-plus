

import player
import window



if __name__=="__main__":

    #  音频可视化 "--audio-visual=visual", "--effect-list=spectrum", "--effect-fft-window=flattop"
    print("start")

    playerlist=[None]*9
    for key in range(9):
        playerlist[key]=player.Player()

    win=window.CreateWindows()
    win.transmit_player(playerlist)
    win.create_video_view()

    for key in range(9):

        playerlist[key].play("http://113.106.101.202/0_eb204c21c0d8fc5b7ffac93462050c22.mp4?type=client&vvid=4FE0747B-4FE9-40E6-B9C7-2467DBE0F700&k=7998e5919e9def757af105fb3a7581c2-3246-1587913630%26bppcataid%3D17&cltver=5.1.1.0002&agent=ppap")

    #win.player1.play("../../test.ts")
    #win.player2.play("../../test.ts")
    #win.player3.play("../../test.ts")
    #win.player4.play("../../test.ts")

    win.mainloop()



