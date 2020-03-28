from tkinter import *
from tkinter import filedialog
import numpy as np
from ocr import mnist
from skimage.color import rgb2gray
from PIL import Image
import PIL.ImageOps

root = Tk()
root.title("OCR Project")
root.geometry('700x400')

lbl = Label(root, text='')
lbl.grid(row=0, column=1)


def invert(arr1, img1):
    total = 0

    for i, item in enumerate(arr1[0][:]):
        total += arr1[0][i]

    if total < 3000:
        inverted_image = PIL.ImageOps.invert(img1)
        return inverted_image
        # inverted_image.save('hello.jpg')
        # print('black')
        # print('total is ----------- ' + str(total))
    else:
        # img1.save('hello.jpg')
        # print('white')
        # print('total is ----------- ' + str(total))
        return img1
    


def select_file():
    file = filedialog.askopenfile()
    cover, image = mnist.resize_img(file.name)
    # cover.save(file.name.split('/')[-1], image.format)

    path = './ocr/model.sav'
    model = mnist.load_model(path)

    img_arr = np.array(cover)
    img_arr_2d = rgb2gray(img_arr)

    img_arr_invert = invert(img_arr_2d, cover)
    img_arr_again = np.array(img_arr_invert)
    img_reshaped_arr = img_arr_again.reshape(1, -1)

    number = model.predict(img_reshaped_arr)
    lbl.configure(text='The number is: ' + str(number[0]))


btn = Button(root, text="Select File", command=select_file)
btn.grid(row=0, column=0)

root.mainloop()
