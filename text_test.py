import os

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from cv2 import VideoWriter_fourcc

d = {}

for i in range(32, 127):
  image = np.ones((100, 60))*255
  font = ImageFont.truetype("""C:\\Users\\popme\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Cascadia.ttf""", 96, encoding='utf-8')
  frame = Image.fromarray(image)
  draw = ImageDraw.Draw(frame)
  draw.text((0,0), chr(i), '#000000', font, align='center')
  cv2Image = np.array(frame)
  result = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2BGR)
  avg = np.average(result)
  d[chr(i)] = int(avg)

items=  d.items()

print(len(items))
backItems = [[v[1], v[0]] for v in items]
backItems.sort()

actualResult = {}
for item in backItems:
  actualResult[item[0]] = item[1]

for i in range(0, 256):
  actualResult[i] = backItems[min(95,int(i/256*95))][1]

for i in range(0, 256):
  print(actualResult[i])

print(actualResult)




