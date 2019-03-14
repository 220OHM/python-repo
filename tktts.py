from tkinter import *
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.spVoice")


def hi():
    ts = ent.get()
    speak.Speak(ts)


root = Tk()
but = Button(root, text="Spreche!", command=hi)
lab = Label(root, text="Was soll ich sagen.")
ent = Entry()
lab.pack()
ent.pack()
but.pack()
root.mainloop()
