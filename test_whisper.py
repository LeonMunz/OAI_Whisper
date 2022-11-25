import os
import whisper

# Path to audio file
audio = os.path.join('audio', 'test_audio.mp3')

# Load model
model = whisper.load_model('base')
# Read the entire file and processes the audio
res = model.transcribe(audio)
# Print out result
print(res['text'])

