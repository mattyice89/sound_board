# Need to install pip install git+https://github.com/jpercent/pyttsx.git

# ME: I had fun playing with this first part (pyttsx), but it seems
# like the mp3 sound quality is a bit better
"""
import pyttsx
engine = pyttsx.init()
engine.setProperty('rate',200)
engine.setProperty('voice', 3)
engine.say("I'll take a liter of cola.");
engine.runAndWait();
"""

import subprocess
from gtts import gTTS

# Prompting for the customer name before everything is read
Customer_Name = raw_input("Enter Customer Name >>")

audio_file = "newcustomer.mp3"
audio_file2 = "Customername.mp3"
airhorn = "airhorn.mp3"
cantstop = "icantstopclip.mp3"

tts = gTTS(text="We just signed ")
tts.save(audio_file)
tts = gTTS(text= Customer_Name)
tts.save(audio_file2)

return_code = subprocess.call(["afplay", airhorn])
return_code = subprocess.call(["afplay", audio_file])
return_code = subprocess.call(["afplay", audio_file2])
return_code = subprocess.call(["afplay", cantstop])


"""
def convert_text_to_audio(text_to_convert):
    audio_file = ("%s.mp3" % (text_to_convert[:20]))
    tts = gTTS(text=text_to_convert, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["mpg123", audio_file]) # mpg123 is the local audio player
    return return_code

convert_text_to_audio('Hello world')
"""
