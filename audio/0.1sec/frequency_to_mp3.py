import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment

# Define the sample rate and duration of the audio clip
sample_rate = 44100
duration = 0.1  # seconds

# Define the frequencies to be played
freq1 = 700  # A4 note
freq2 = 53  # A5 note

# Generate the audio data from the frequencies
t = np.linspace(0, duration, int(duration * sample_rate), False)
data = np.sin(freq1 * 2 * np.pi * t) + np.sin(freq2 * 2 * np.pi * t)
data = data * (2**15 - 1) / np.max(np.abs(data))
data = data.astype(np.int16)

# Write the audio data to a wav file
wavfile.write('output.wav', sample_rate, data)

# Load the wav file into an AudioSegment object
audio = AudioSegment.from_wav('output.wav')

# Convert the AudioSegment object to an mp3 file
audio.export('g.mp3', format='mp3')
