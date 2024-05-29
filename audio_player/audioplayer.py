import curses
import pygame
import os

def init_curses():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    return stdscr

def end_curses(stdscr):
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def main(stdscr):
    pygame.mixer.init()

    songs = "././songs"
    playlist = [f for f in os.listdir(songs) if f.endswith('.mp3')]
    queue = None

    if not playlist:
        stdscr.addstr(0, 0, "Spotify-spotifyan\nGa ada lagu anjay donlot dulu")
        stdscr.refresh()
        stdscr.getch()
        return

    while True:
        stdscr.clear()

        if queue is not None:
            current_song = playlist[queue]
            stdscr.addstr(0, 0, f"Lagi diputer: {current_song}")
        else:
            stdscr.addstr(0, 0, "Lagi diputer: ")

        stdscr.addstr(2, 0, "Spotify-spotifyan\nPencet aja bang kalo mau muter lagu\np - Play, s - Stop, n - Next, q - Quit")

        key = stdscr.getch()

        if key == ord('p'):
            if queue is None:
                queue = 0
            current_song = playlist[queue]
            pygame.mixer.music.load(os.path.join(songs, current_song))
            pygame.mixer.music.play()
        elif key == ord('s'):
            pygame.mixer.music.stop()
        elif key == ord('n'):
            if queue is not None:
                queue += 1 % len(playlist)
                current_song = playlist[queue]
                pygame.mixer.music.load(os.path.join(songs, current_song))
                pygame.mixer.music.play()
        elif key == ord('q'):
            break

        stdscr.refresh()

if __name__ == "__main__":
    stdscr = init_curses()
    try:
        main(stdscr)
    finally:
        end_curses(stdscr)
        pygame.mixer.quit()
