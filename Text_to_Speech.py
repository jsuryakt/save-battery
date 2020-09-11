from gtts import gTTS
import os

#Enter the text which you want to convert into audio file
#Here I want audio files connect.mp3 and disconnect.mp3
#Note : Change "Sunil" with your own name

myText1 = "Sunil, Please connect the charger"
myText2 = "Sunil, Please Disconnect the charger"

#Specify the language en indicates English
language = "en"

#gTTS method converts text into audio format
output1 = gTTS(text = myText1, lang = language, slow = False)
output2 = gTTS(text = myText1, lang = language, slow = False)

output1.save("connect.mp3")
output2.save("disconnect.mp3")
