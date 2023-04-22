from pydub import AudioSegment
import os

# Define the file names to be appended
file_names = ['a.mp3', 'b.mp3', 'c.mp3','d.mp3','e.mp3','f.mp3','g.mp3','h.mp3','i.mp3','j.mp3','k.mp3','l.mp3','m.mp3','n.mp3','o.mp3','p.mp3','q.mp3','r.mp3','s.mp3','t.mp3','u.mp3','v.mp3','w.mp3','x.mp3','y.mp3','z.mp3']

# Create an empty audio segment object
output_audio = AudioSegment.empty()

# Iterate over the file names and append the audio segments to the output audio object
for file_name in file_names:
    audio = AudioSegment.from_file(file_name, format='mp3')
    output_audio += audio

# Export the output audio to a new mp3 file
output_audio.export('alphabet.mp3', format='mp3')

