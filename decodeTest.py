import numpy as np
from pydub import AudioSegment
from scipy import fft
import os

# Define the path to the audio file
audio_path = 'combined_audio.mp3'

# Load the audio file into an AudioSegment object
audio_segment = AudioSegment.from_file(audio_path, format='mp3')

# Define the window size and slice size in milliseconds
window_size = 1000  # 1 second
slice_size = 1000  # 1 second

# Convert the AudioSegment object to a numpy array
audio_array = np.array(audio_segment.get_array_of_samples())

# Calculate the number of slices
num_slices = int(np.ceil(len(audio_array) / slice_size))

# Create an empty list to store the Fourier transforms
fft_list = []

# Loop over the slices and calculate the Fourier transform of each slice
for i in range(num_slices):
    # Extract the slice from the audio array
    slice_start = i * slice_size
    slice_end = slice_start + window_size
    slice_array = audio_array[slice_start:slice_end]

    # Apply the Fourier transform to the slice
    fft_array = fft(slice_array)

    # Append the Fourier transform to the list
    fft_list.append(fft_array)

# Convert the list of Fourier transforms to a numpy array
fft_array = np.array(fft_list)

# Save the numpy array to a file
np.save('audio_fft.npy', fft_array)

