from PIL import Image

from resizeimage import resizeimage


with open('six.jpg', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [28, 28])
        cover.save('test-image-cover.jpg', image.format)