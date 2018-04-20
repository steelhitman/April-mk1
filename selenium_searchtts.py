from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
import mp3play
from mutagen.mp3 import MP3
import sys
import time
from time import ctime
import os
from gtts import gTTS
global text
text=""
tts = gTTS(text="what to search for ?", lang='en')
tts.save("search.mp3")
f="search.mp3"
audio = MP3(f)
length=audio.info.length    
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()

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
    with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
        r.adjust_for_ambient_noise(source)
        print "Say search keywork..."
        
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print "you said: " + text
        except:
            pass
        if text!="":
            break
        
driver = webdriver.Chrome(executable_path=r"C:\Python27\april\chromedriver.exe")
driver.get("https://www.wikipedia.org/")
elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys(text)
elem.send_keys(Keys.ENTER)
data=driver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[1]").text
print data
#assert "No results found." not in driver.page_source
driver.close()
tts = gTTS(text=data, lang='en')
tts.save("result.mp3")
f="result.mp3"
audio = MP3(f)
length=audio.info.length
clip = mp3play.load(f)
clip.play()
time.sleep(length)
clip.stop()
