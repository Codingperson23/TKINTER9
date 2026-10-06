from tkinter import*
from tkinter import messagebox
from PIL import *
window = Tk()
window.title("My photo albu m")
window.geometry('420x400')
title = Label(window, text="My photo album", font=("Arial Bold", 20))
title.pack(pady=20)
img_file = Image.open('image.jpg')
img_file = img_file.resize((300, 200))
photo = ImageTk.PhotoImage(img_file)
img_label = Label(window, image=photo)
img_label.pack(pady=5)

def show_message():