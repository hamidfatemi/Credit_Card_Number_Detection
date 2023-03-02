# Morphological filtering
from skimage.morphology import opening
from skimage.morphology import disk

# Data handling
import numpy as np

# Connected component filtering
import cv2
from PIL import Image

#read the image from path
image = Image.open('./text_document.jpeg')
#Converting the same image to black and white mode
BW= image.convert('1')
#save both the images
BW.save("BW_image.jpg")

black = 0
white = 255
threshold = 127

# Open input image in grayscale mode and get its pixels.
img = Image.open("./BW_image.jpg").convert("LA")
pixels = np.array(img)[:,:,0]

# Remove pixels above threshold
pixels[pixels > threshold] = white
pixels[pixels < threshold] = black


# Morphological opening
blobSize = 1 # Select the maximum radius of the blobs you would like to remove
structureElement = disk(blobSize)  # you can define different shapes, here we take a disk shape
# We need to invert the image such that black is background and white foreground to perform the opening
pixels = np.invert(opening(np.invert(pixels), structureElement))


# Create and save new image.
newImg = Image.fromarray(pixels).convert('RGB')
newImg.show()
newImg.save("result.jpeg")




