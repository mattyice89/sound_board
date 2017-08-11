# Need to install pip install git+https://github.com/jpercent/pyttsx.git

Quotes = (
    "I'll have a liter of cola.",
    "Give me a god damn liter of cola.",
    "You boys like Mex e co?",
    "All right meow, hand over your license and registration.",
    "License and registration... chicken fucker!",
    "Say car ram rod.  Say Car Ram Rod... You didn't say it.  Oh I forgot.  I wrote it on the sign.  Oh yeah...",
    "Do I look like a cat to you, boy?  Do you see me running around all nimbly bimbly from tree to tree?  Am I drinking milk from a saucer?",
    "Littering and... Littering and...",
    "I'm freaking out man!  Yes, you are freaking out, man!",
    "These boys get that syrup in them and they get all antsy in their pantsy.",
)

import random

Sentence = raw_input("Type in what you want to say> ")
print(Sentence)

import pyttsx
engine = pyttsx.init()
engine.setProperty('rate',200)
engine.say(Sentence);
engine.runAndWait();
exit()

"""
audio_file = "hello.mp3"
tts = gTTS(text="Hello Imig", lang="en")
tts.save(audio_file)
return_code = subprocess.call(["afplay", audio_file])


import subprocess
from gtts import gTTS


def convert_text_to_audio(text_to_convert):
    audio_file = ("%s.mp3" % (text_to_convert[:20]))
    tts = gTTS(text=text_to_convert, lang="en")
    tts.save(audio_file)
    return_code = subprocess.call(["mpg123", audio_file]) # mpg123 is the local audio player
    return return_code

convert_text_to_audio('Hello world')
"""
