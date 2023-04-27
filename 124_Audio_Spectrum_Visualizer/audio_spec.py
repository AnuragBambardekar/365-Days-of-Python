import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

from scipy.fftpack import fft

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate = RATE,
	input=True,
	output=True,
	frames_per_buffer=CHUNK
)
fig, (ax, ax2) = plt.subplots(2, figsize=(7, 5))

x = np.arange(0, 2*CHUNK, 2)
line, =ax.plot(x, np.random.rand(CHUNK))

x_fft = np.linspace(0, RATE, CHUNK)
#line_fft, = ax2.plot(x_fft, np.random.rand(CHUNK), '-')
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK), '-')

ax.set_ylim(-128, 128)
ax.set_xlim(0, CHUNK)

ax2.set_xlim(20, RATE / 2)

fig.show()

while True:
	data = stream.read(CHUNK)
	data_int = np.array(struct.unpack(str(2*CHUNK) + 'B', data), dtype='b')[::2]
	line.set_ydata(data_int)

	y_fft = fft(data_int)
	line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) * 2 / (128*CHUNK) )

	fig.canvas.draw()
	fig.canvas.flush_events()
