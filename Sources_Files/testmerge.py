from pydub import AudioSegment
import os

# Set the directory where the audio files are located
audio_dir = "/home/tytionex/Documents/EE250Project/audio/other"

# Get a list of all audio files in the directory
audio_files = [f for f in os.listdir(audio_dir) if f.endswith(".mp3")]

# Sort the list of audio files alphabetically
audio_files.sort()

# Initialize an empty AudioSegment object to store the combined audio
combined_audio = AudioSegment.empty()

# Loop through each audio file and append it to the combined audio object
for audio_file in audio_files:
    # Load the audio file into an AudioSegment object
    audio = AudioSegment.from_file(os.path.join(audio_dir, audio_file), format="mp3")
    
    # Append the audio to the combined audio object
    combined_audio = combined_audio + audio

# Export the combined audio as an mp3 file
combined_audio.export("combined_audio.mp3", format="mp3")

