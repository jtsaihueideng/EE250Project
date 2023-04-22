from pydub import AudioSegment
import os

# Define the file names to be appended
file_names = ['h.mp3', 'e.mp3', 'l.mp3','l.mp3','o.mp3']

# Create an empty audio segment object
output_audio = AudioSegment.empty()

# Iterate over the file names and append the audio segments to the output audio object
for file_name in file_names:
    audio = AudioSegment.from_file(file_name, format='mp3')
    output_audio += audio

# Export the output audio to a new mp3 file
output_audio.export('combined_audio.mp3', format='mp3')

