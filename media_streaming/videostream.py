import vlc
import time

def play_media(file_path):
    instance = vlc.Instance('..no-xlib')
    player = instance.media_player_new()
    media = instance.media_new(file_path)
    player.set_media(media)
    player.play()

    while player.get_state() != vlc.State.Ended:
        time.sleep(1)
    player.stop()

    instance.release()

media_file_path = "././videos/ubur_ubur.mp4"
play_media(media_file_path)