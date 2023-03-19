from tkinter import * 
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text To Speech")
root.geometry("1000x500")
root.resizable(False, False)
root.configure(bg="#6666ff")

bar_icon = PhotoImage(file = "mic.png")
root.iconphoto(False,bar_icon)

engine = pyttsx3.init()

def speakNow():
    text = type_area.get(1.0, END)
    gender = genderbox.get()
    speed = speedbox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if gender == "Male":
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if text:
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 50)
            setvoice()

def download():
    text = type_area.get(1.0, END)
    gender = genderbox.get()
    speed = speedbox.get()
    voices = engine.getProperty("voices")

    def setvoice():
        if gender == "Male":
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
    if text:
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 50)
            setvoice()

# upper frame
Top_frame = Frame(root,bg = "#e6e6ff", width = 1000, height = 130).place(x = 0, y = 0)
logo = PhotoImage(file = "mic.png")
Label(Top_frame, image = logo, bg = "#e6e6ff").place(x = 10, y = 10)
Label(Top_frame, text="TEXT TO SPEECH", font="Dungeon 30 bold",bg = "#e6e6ff", fg = "black").place(x = 150, y = 40)

type_area = Text(root, font = "Papyrus 15 bold", bg = "white", relief = GROOVE, wrap = WORD)
type_area.place(x = 20, y = 180, width = 500, height = 300)

Label(root, text = "Voice", font = "Sylfaen 15 bold", bg = "#6666ff", fg = "#e6e6ff").place(x = 610, y = 160)
genderbox = Combobox(root, values=["Male", "Female"], font = "Sylfaen 12 bold", state = 'r', width = 15)
genderbox.place(x = 570, y = 200)
genderbox.set("Male")

Label(root, text = "Speed", font = "Sylfaen 15 bold", bg = "#6666ff", fg = "#e6e6ff").place(x = 840, y = 160)
speedbox = Combobox(root, values=["Fast", "Normal", "Slow"], font = "Sylfaen 12 bold", state = 'r', width = 15)
speedbox.place(x = 800, y = 200)
speedbox.set("Normal")

# Speak button
speak_btn = PhotoImage(file = "speaking.png")
speak_img_label = Label(image = speak_btn)
speak_button = Button(root, image = speak_btn, bg = "#6666ff", command = speakNow).place(x = 600, y = 280)

# Save button
save_btn = PhotoImage(file = "save.png")
save_img_label = Label(image = save_btn)
save_button = Button(root, image = save_btn, bg = "#6666ff", command = download).place(x = 830, y = 280)

root.mainloop()
