from tkinter import *
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.spVoice")


def hi():  # speaking bits
    ts = ent.get()
    speak.Speak(ts)


root = Tk()  # GUI bits
root.title("tktts")
but = Button(root, text="Speak!", command=hi)
lab = Label(root, text="What should i say?")
ent = Entry()
lab.pack()
ent.pack()
but.pack()
root.mainloop()
