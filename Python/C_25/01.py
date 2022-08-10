from PIL import Image


def showimage(image):
    im = Image.open(f"./pics/{image}.png")
    width, height = im.size
    left = 5
    top = height
    right = 164
    bottom = width
    im1 = im.crop((left, top, right, bottom))
    im1.show()


showimage("dog")
