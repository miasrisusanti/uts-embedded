import pyaudio
import numpy as np
import pygame
import wave
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

music_file = '././songs/kucing.wav'
file_name = os.path.basename(music_file)
pygame.display.set_caption(f"{file_name}")

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

music_file = '././songs/kucing.wav'
wf = wave.open(music_file, 'rb')

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

def draw_spectrum(data):
    screen.fill((0, 0, 0))
    spectrum = np.abs(np.fft.fft(data))[:len(data)//2] / (128 * len(data))
    for i, magnitude in enumerate(spectrum):
        pygame.draw.line(screen, (255, 255, 255), (i, 600), (i, 600 - int(magnitude * 600)), 1)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = wf.readframes(CHUNK)
    if len(data) == 0:
        break

    data_int = np.frombuffer(data, dtype=np.int16)

    draw_spectrum(data_int)

    stream.write(data)

stream.stop_stream()
stream.close()
p.terminate()
wf.close()

pygame.quit()
