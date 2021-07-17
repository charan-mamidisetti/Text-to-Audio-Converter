"""First we need to install two modules called- "gTTs" and "playsound".
for that just write "pip install gTTS" in command promt. And the Module will get Installed
Same with "playsound" module"""
# Now in Virtual Studio or any Ide....

from gtts import gTTS         # To import gTTs module into the python(py) file.
from playsound import playsound        # To import playsound module into the py file
audio="speech.mp3"          # Need to create a file("audio" in my code) and assign a .mp3 address to it.
language="en"       # To specify the language of text.
sp=text("Hey there!",lang=language,slow=False)      # Text=Hey there!, slow is basically a keyword to specify whether we need audio to be slow or fast.
sp.save(audio)      # To save the sp file for audio
playsound(audio)      #To play audio
print("The Audio is playing....")     # To just print a line and to know whether the audio is playing( Not actually nessasary)
