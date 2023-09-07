import tkinter
import customtkinter as CTLib
from pytube import YouTube

def setType(choice):
    global downloadtype
    downloadtype = choice
    print(downloadtype)

def startDownload():
    print(downloadtype)


CTLib.set_appearance_mode("dark")
CTLib.set_default_color_theme("blue")

app = CTLib.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = CTLib.CTkLabel(app, text="Paste Youtube link here!")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = CTLib.CTkEntry(app, width=450, height=40, textvariable=url)
link.pack()

typeMenu = CTLib.CTkOptionMenu(app, values=['MP4','MP3'], command=setType)
typeMenu.set("MP4")
typeMenu.pack()

download = CTLib.CTkButton(app, text="Download", command=startDownload)
download.pack()

app.mainloop()