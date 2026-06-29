# This program will remind after an hour to drink water by speaking


import time 
import win32com.client

speaker = win32com.client.Dispatch("Sapi.SpVoice")
i = 0
while True:
    time.sleep(3600)
    i = i + 1
    speaker.Speak("Hello! I am your virtual assistant. It's time to drink water!")
