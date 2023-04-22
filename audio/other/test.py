import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment

# Define the sample rate and duration of the audio clip
sample_rate = 44100
duration = 1  # seconds
ch = 'a'

# Define the frequencies to be played
freq1 = 100  # A4 note
freq2 = 1653  # A5 note
for x in range(13):
    # Generate the audio data from the frequencies
    t = np.linspace(0, duration - 1/sample_rate, int(duration * sample_rate), False)
    data = np.sin(freq1 * 2 * np.pi * t) + np.sin(freq2 * 2 * np.pi * t)
    data = data * (2**15 - 1) / np.max(np.abs(data))
    data = data.astype(np.int16)

    # Write the audio data to a wav file
    wavfile.write('output.wav', sample_rate, data)

    # Load the wav file into an AudioSegment object
    audio = AudioSegment.from_wav('output.wav')

    # Convert the AudioSegment object to an mp3 file
    audioFileName = ch + '.mp3'
    audio.export(audioFileName, format='mp3')
    ch = chr(ord(ch) + 1)
    freq1 += 100

freq1 = 100  # A4 note
freq2 = 1987  # A5 note
for x in range(13):
    # Generate the audio data from the frequencies
    t = np.linspace(0, duration - 1/sample_rate, int(duration * sample_rate), False)
    data = np.sin(freq1 * 2 * np.pi * t) + np.sin(freq2 * 2 * np.pi * t)
    data = data * (2**15 - 1) / np.max(np.abs(data))
    data = data.astype(np.int16)

    # Write the audio data to a wav file
    wavfile.write('output.wav', sample_rate, data)

    # Load the wav file into an AudioSegment object
    audio = AudioSegment.from_wav('output.wav')

    # Convert the AudioSegment object to an mp3 file
    audioFileName = ch + '.mp3'
    audio.export(audioFileName, format='mp3')
    ch = chr(ord(ch) + 1)
    freq1 += 100
	
