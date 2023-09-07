import tkinter
from tkinter import filedialog
import customtkinter as CTLib
from pytube import YouTube as YT
from threading import Thread

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YT(ytLink, on_progress_callback=progress)
        video = ytObject.streams.get_by_resolution(qualityMenu.get())
        title.configure(text=ytObject.title)
        folder_path = filedialog.askdirectory()
        video.download(output_path=folder_path, filename=f"{video.title}." + typeMenu.get())
        # MsgLabel.configure(text="Download was Complete!", text_color="white")
        ProgressLabel.configure(text="Download Complete!", text_color="white")
    except:
        ProgressLabel.configure(text="Download Error!", text_color="red")
        # MsgLabel.configure(text="Download Error!", text_color="red")

def progress(stream, chunk, bytes_remaning):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaning
    procentage_downloaded = bytes_downloaded / total_size * 100
    pro = str(int(procentage_downloaded))

    ProgressLabel.configure(text=pro + "%")
    ProgressLabel.update()

    ProgressBar.set(float(procentage_downloaded) / 100)

CTLib.set_appearance_mode("dark")
CTLib.set_default_color_theme("blue")

app = CTLib.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")
app.resizable(False, False)

title = CTLib.CTkLabel(app, text="Paste Youtube link here!", font=("Arial", 20))
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = CTLib.CTkEntry(app, width=450, height=40, textvariable=url, font=("Arial", 12))
link.pack()

# MsgLabel = CTLib.CTkLabel(app, text="", font=("Arial", 12))
# MsgLabel.pack()

ProgressLabel = CTLib.CTkLabel(app, text="0%", font=("Arial", 12))
ProgressLabel.pack(padx=10, pady=10)

ProgressBar = CTLib.CTkProgressBar(app, width=500)
ProgressBar.set(0)
ProgressBar.pack(padx=10, pady=10)

typeMenu = CTLib.CTkOptionMenu(app, values=['mp4','mp3'], font=("Arial", 12))
typeMenu.set("mp4")
typeMenu.pack(padx=10, pady=10)

qualityMenu = CTLib.CTkOptionMenu(app, values=['720p', '480p', '360p', '240p', '144p'], font=("Arial", 12))
qualityMenu.set("720p")
qualityMenu.pack(padx=10, pady=10)

download = CTLib.CTkButton(app, text="Download", command=startDownload, font=("Arial", 12))
download.pack(padx=10, pady=10)

app.mainloop()