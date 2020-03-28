from PIL import Image
import PIL.ImageOps
import numpy as np

imgname = './ocr/img_2.jpg'
img1 = Image.open(imgname)
arr1 = np.array(img1)

total = 0

for i, item in enumerate(arr1[0][:]):
    total += arr1[0][i]

if total < 1000:
    inverted_image = PIL.ImageOps.invert(img1)
    inverted_image.save('hello.jpg')
    print('black')
    print('total is ----------- ' + str(total))
else:
    img1.save('hello.jpg')
    print('white')
    print('total is ----------- ' + str(total))









# from PIL import Image
# import PIL.ImageOps    

# image = Image.open('your_image.png')

# inverted_image = PIL.ImageOps.invert(image)

# inverted_image.save('new_name.png')