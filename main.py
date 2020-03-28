from tkinter import *
from tkinter import filedialog
import numpy as np
from ocr import mnist

root = Tk()
root.title("OCR Project")
root.geometry('700x400')

lbl = Label(root, text='')
lbl.grid(row=0, column=1)


def select_file():
    file = filedialog.askopenfile()
    cover, image = mnist.resize_img(file.name)

    path = './ocr/model.sav'
    model = mnist.load_model(path)

    img_arr = np.array(cover)
    img_reshaped = img_arr.reshape(1, -1)

    number = model.predict(img_reshaped)
    lbl.configure(text='The number is: ' + str(number[0]))


btn = Button(root, text="Select File", command=select_file)
btn.grid(row=0, column=0)

root.mainloop()
