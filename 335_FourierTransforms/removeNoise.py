"""
create an audio signal with a high pitched buzz in it, and then remove the buzz using the Fourier transform
"""

import numpy as np
from matplotlib import pyplot as plt

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi because np.sin takes radians
    y = np.sin((2 * np.pi) * frequencies)
    return x, y

# Generate a 2 hertz sine wave that lasts for 5 seconds
x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()

_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
noise_tone = noise_tone * 0.3

mixed_tone = nice_tone + noise_tone

# Due to how we'll store the audio later, the target format is a 16-bit integer, which has a range from -32768 to 32767
normalized_tone = np.int16((mixed_tone / mixed_tone.max()) * 32767)

plt.plot(normalized_tone[:1000])
plt.show()

from scipy.io.wavfile import write

# Remember SAMPLE_RATE = 44100 Hz is our playback rate
write("mysinewave.wav", SAMPLE_RATE, normalized_tone)

from scipy.fft import fft, fftfreq

# Number of samples in normalized_tone
N = SAMPLE_RATE * DURATION

# Calculating the Fourier Transform
yf = fft(normalized_tone) # calculates the transform itself
xf = fftfreq(N, 1 / SAMPLE_RATE) # calculates the frequencies in the center of each bin in the output of fft()
# A bin is a range of values that have been grouped, like in a histogram.

plt.plot(xf, np.abs(yf))
"""
can see two peaks in the positive frequencies and mirrors of those peaks in the negative frequencies. 
The positive-frequency peaks are at 400 Hz and 4000 Hz, which corresponds to the frequencies that you put into the audio.
The negative-positive symmetry is a side effect of putting real-valued input into the Fourier transform
"""
plt.show()





