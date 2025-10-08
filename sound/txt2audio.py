from gtts import gTTS
import os
outtext = "/Users/linaliu/code/scratch/sound/vivian.mp3"
text = "/Users/linaliu/code/scratch/sound/vivian.txt"
#with open(text, 'r') as f:
#    lines = f.readlines()

#text_content = ''.join(lines)
text_content = "vivian"
# Create a gTTS object
tts = gTTS(text_content, lang='en')

# Save the audio file
tts.save(outtext)


