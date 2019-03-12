import time
import datetime
import random
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.spVoice")  # starts the windows tts
speak.Volume = 100
sd = time.time()
fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
tg = 1
while True:
    gd = random.randint(1, 5)  # random number
    dr = time.time()
    rd = datetime.datetime.fromtimestamp(dr).strftime('%H')  # unix clock
    print(rd)
    if fd < rd:  # jokes starts here ps: you can change them to your langunge
        if gd == 1:
            speak.Speak("Wo leben die meisten Gespenster,In BUHdapest.")
            print(rd)
            sd = time.time()
            fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
        elif gd == 2:
            speak.Speak("Wie war die Stimmung in der DDR,Sie hielt sich ziemlich in Grenzen.“")
            print(rd)
            sd = time.time()
            fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
        elif gd == 3:
            speak.Speak("Wann gehen U-Boote unter,Am Tag der offenen Tür.")
            print(rd)
            sd = time.time()
            fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
        elif gd == 4:
            speak.Speak("Was hat einer der im Dreieck läuft,Kreislaufprobleme")
            print(rd)
            sd = time.time()
            fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
        elif gd == 5:
            speak.Speak("Egal was du hast,Bruce Will’s")
            print(rd)
            sd = time.time()
            fd = datetime.datetime.fromtimestamp(sd).strftime('%H')
    print(rd)
    time.sleep(1)
    tg += 1  # btw this is dumb
