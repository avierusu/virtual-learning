# This program will create an animated gif from image files
# by toggling between them repeatedly

# We want to pass the file names as arguments, so import sys
import sys
# Import support for images from pillow
from PIL import Image
# I had to manually disable the requirement for jpeg for this to work

images = []

# We loop through excluding argv[0] because that is the file name
for arg in sys.argv[1:]:
    # Store the image files passed as arguments
    image = Image.open(arg)
    images.append(image)


# Save the file to the disk
images[0].save(
    # save_all will save every frame to the gif file
    # We then append the next image using append_images
    # We set the duration of each frame to 200ms
    # setting loop=0 will loop it infinitely
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)


# We run the following command to test this code:
#   python costumes.py costume-1.gif costume-2.gif