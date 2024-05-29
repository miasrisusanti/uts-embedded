import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import wave
import os
import threading

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

music_file = '././songs/kucing.wav'
wf = wave.open(music_file, 'rb')

audio_buffer = np.zeros(CHUNK, dtype=np.int16)

def audio_callback(in_data, frame_count, time_info, status):
    global audio_buffer, wf
    data = wf.readframes(frame_count)
    if len(data) < frame_count * wf.getsampwidth():
        wf.rewind()
        data += wf.readframes(frame_count - len(data) // wf.getsampwidth())
    audio_buffer = np.frombuffer(data, dtype=np.int16)
    return (data, pyaudio.paContinue)

fig, ax = plt.subplots()
x = np.arange(0, CHUNK // 2)
line, = ax.plot(x, np.random.rand(CHUNK // 2))
ax.set_ylim(0, 1)
ax.set_xlim(0, CHUNK // 2)

file_name = os.path.basename(music_file)
fig.suptitle(f"{file_name}")

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=audio_callback)

def update(frame):
    global audio_buffer
    data_int = audio_buffer
    spectrum = np.abs(np.fft.fft(data_int))[:CHUNK // 2] / (128 * CHUNK)
    line.set_ydata(spectrum)
    return line,

ani = FuncAnimation(fig, update, blit=True)

def start_stream():
    stream.start_stream()
    while stream.is_active():
        pass

audio_thread = threading.Thread(target=start_stream)
audio_thread.start()

plt.show()
