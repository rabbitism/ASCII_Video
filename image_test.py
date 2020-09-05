import os

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from cv2 import VideoWriter_fourcc

image_dir = os.path.sep.join(['.', 'Picture1.png'])
 
image = cv2.imread(image_dir)

print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(np.sum(gray))

# order is blue green red
blue, green, red = cv2.split(image)
print(np.average(red))
print(np.average(green))
print(np.average(blue))

rgb_order_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

frame = Image.fromarray(gray)

font = ImageFont.truetype("""C:\\Users\\popme\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Cascadia.ttf""", 8, encoding='utf-8')

draw = ImageDraw.Draw(frame)

draw.text((0,0), "B", '#555555', font)
draw.text((0,8), "B", '#555555', font)
draw.text((6,0), "C", '#555555', font)
draw.text((6,8), "C", '#555555', font)

cv2Image = np.array(frame)
result = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2BGR)

cv2.imwrite('test.png', result)
