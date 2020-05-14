import window

import pleyer_top
if __name__ == "__main__":

    play=pleyer_top.PlayerTop()
    win = window.CreateWindows()
    win.transmit_player(play.playerlist)
    win.create_video_view()
    play.play_start()
    win.refresh_windows()
    win.mainloop()
