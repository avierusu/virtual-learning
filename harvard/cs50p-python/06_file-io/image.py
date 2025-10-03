# This program will demonstrate some funcionalities of the
# Pillow library
# First, we will rotate an image file

from PIL import Image

def main():
    # Open our image file using its full file path
    with Image.open("C:\\virtual-learning\harvard\cs50p-python\\06_file-io\in.jpg") as img:
        # .size returns the pixel dimensions of the image
        print(img.size)
        # .format returns the file format
        print(img.format)
        # rotate() will rotate the image by a certain number of degrees
        img.rotate(180)
        # We can save the updated (rotated) image using save()
        img.save("C:\\virtual-learning\harvard\cs50p-python\\06_file-io\out.jpg")


main()