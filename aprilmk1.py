import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
import time
from time import ctime
import time
import os
from gtts import gTTS

def rest():
    tts = gTTS(text="If you need me, I'll be around", lang='en')
    tts.save("rest.mp3")
    f="rest.mp3"
    audio = MP3(f)
    length=audio.info.length
    clip = mp3play.load(f)
    clip.play()
    time.sleep(length)
    clip.stop()
    
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:
        while True:
            try:
                r.adjust_for_ambient_noise(source)
                print "In silent Mode..."
        
                audio = r.listen(source)
                text = r.recognize_google(audio)
                if text=="wake up jarvis":
                    break
                else:
                    pass
            except:
                pass

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("start audio_out.py")

speak("It's a pleasure to have you back")
f="audio.mp3"
audio = MP3(f)
length=audio.info.length
time.sleep(length)

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()
 
mic_list = sr.Microphone.list_microphone_names()

device_id = 0

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
while True:
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, 
                            chunk_size = chunk_size) as source:
        
        r.adjust_for_ambient_noise(source)
        print "Say Something"
        
        audio = r.listen(source)
             
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
            inp=list(text.split(' '))
            if inp[0]=="Jarvis" or inp[0]=="jarvis":
                print "Listening..."
                #audio=r.listen(source)
                #text = r.recognize_google(audio)
                #print "you said: " + text
                text=text.lower()
                if text=="jarvis what's the date":# or text=="what is the date" or "tell the date":
                    os.system("start date.py")
                    #date()
                    f="date.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)
                
                elif text=="jarvis what's the time":# or text=="what is the time" or "tell the time":
                    os.system("start time_disp.py")
                    #time_disp()
                    f="time.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)
                    
                elif text=="jarvis what day is it":# or text=="what is the time" or "tell the time":
                    os.system("start day.py")
                    #time_disp()
                    f="day.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)

                elif text=="jarvis start an online search":# or text=="what is the time" or "tell the time":
                    os.system("start selenium_searchtts.py")
                    #time_disp()
                    f="search.mp3"
                    audio = MP3(f)
                    length=audio.info.length
                    time.sleep(length)
                    #f="result.mp3"
                    #audio = MP3(f)
                    #length=audio.info.length
                    #time.sleep(length)
                
                elif text=="jarvis have some rest":# or text=="what is the time" or "tell the time":
                    rest()
                    
            elif text=="nice work jarvis":
                os.system("start thanq.py")
                f="thanq.mp3"
                audio = MP3(f)
                length=audio.info.length
                time.sleep(length)
            else:
                pass
                        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
         
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            
