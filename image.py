import os

import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from cv2 import VideoWriter_fourcc

selector = {176: '(', 177: '(', 179: ')', 180: ')', 181: 'c', 182: 'c', 183: 'c', 184: 'x', 185: 'x', 186: 'L', 187: 'L', 188: 'L', 189: 'l', 190: 'l', 191: 'l', 192: 'v', 193: 'v', 194: 'v', 195: '?', 197: '*', 198: '*', 199: '*', 200: 'j', 201: 'j', 202: 'j', 203: '|', 204: '|', 205: '=', 206: '=', 207: '=', 208: '\\', 209: '\\', 210: '\\', 211: '/', 212: '/', 213: '+', 214: '+', 216: '>', 217: '>', 219: '<', 220: '<', 221: '!', 222: '!', 229: '~', 232: '-', 233: '-', 237: ';', 240: '_', 241: '_', 242: '_', 246: ',', 247: ',', 248: '`', 255: ' ', 0: 'W', 1: 'W', 2: 'W', 3: 'B', 4: 'B', 5: 'B', 6: '@', 7: '@', 8: '@', 9: '$', 10: '$', 11: 'M', 12: 'M', 13: 'M', 14: '&', 15: '&', 16: '&', 17: '0', 18: '0', 19: '8', 20: '8', 21: '8', 22: 'N', 23: 'N', 24: 'N', 25: 'D', 26: 'D', 27: 'R', 28: 'R', 29: 'R', 30: 'Q', 31: 'Q', 32: 'Q', 33: '#', 34: '#', 35: '#', 36: '%', 37: '%', 38: 'G', 39: 'G', 40: 'G', 41: 'O', 42: 'O', 43: 'O', 44: 'E', 45: 'E', 46: '6', 47: '6', 48: '6', 49: '9', 50: '9', 51: '9', 52: 'm', 53: 
'm', 54: 'H', 55: 'H', 56: 'H', 57: 'K', 58: 'K', 59: 'K', 60: 'b', 61: 'b', 62: '5', 63: '5', 64: '5', 65: 'P', 66: 'P', 67: 'P', 68: 'd', 69: 'd', 70: 'd', 71: 'A', 72: 'A', 73: 'w', 74: 'w', 75: 'w', 76: 'U', 77: 'U', 78: 'U', 79: 'k', 80: 'k', 81: 'S', 82: 'S', 83: 'S', 84: 'g', 85: 'g', 86: 'g', 87: 'h', 88: 'h', 89: 'p', 90: 'p', 91: 'p', 92: 'q', 93: 'q', 94: 'q', 95: '4', 96: '4', 97: '4', 98: '2', 99: '2', 100: '3', 101: '3', 102: '3', 103: 'X', 104: 'X', 105: 'X', 106: 'Z', 107: 'Z', 108: 'e', 109: 'e', 110: 'e', 111: 'V', 112: 'V', 113: 'V', 114: 'a', 115: 'a', 116: 'o', 117: 'o', 118: 'o', 119: 'C', 120: 'C', 121: 'C', 122: 'F', 123: 'F', 124: 'I', 125: 'I', 126: 'I', 127: 'u', 128: 'u', 129: 'u', 130: '7', 131: '7', 132: '7', 133: 's', 134: 's', 135: '[', 136: '[', 137: '[', 138: ']', 139: ']', 140: ']', 141: 'f', 142: 'f', 143: 'n', 144: 'n', 145: 'n', 146: 't', 147: 't', 148: 't', 149: '1', 150: '1', 151: 'J', 152: 'J', 153: 'J', 154: 'i', 155: 'i', 156: 'i', 157: 'z', 158: 'z', 159: 'r', 160: 'r', 161: 'r', 162: 'y', 163: 'y', 164: 'y', 165: 'T', 166: 'T', 167: 'T', 168: 'Y', 169: 'Y', 170: '{', 171: '{', 172: '{', 173: '}', 174: '}', 175: '}', 178: ')', 196: '?', 215: '+', 218: '>', 223: '!', 224: '"', 225: '"', 226: '"', 227: '~', 228: '~', 230: '^', 231: '^', 234: '-', 235: ';', 236: ';', 238: ':', 239: ':', 243: "'", 244: "'", 245: "'", 249: '`', 250: '`', 251: '.', 252: '.', 253: '.', 254: ' '}

class ImageHelper():

  def __init__(self):
    super().__init__()

  @staticmethod
  def split_image(image:np.array):
    blue, green, red = cv2.split(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return red, green, blue, gray

  @staticmethod
  def get_color(red:np.array, green:np.array, blue:np.array, gray:np.array, x:int, y:int, height:int, width: int):
    red_average = np.average(red[x:x+height, y:y+width])
    green_average = np.average(green[x:x+height, y:y+width])
    blue_average = np.average(blue[x:x+height, y:y+width])
    gray_average = np.average(gray[x:x+height, y:y+width])
    if (gray_average<30):
      return gray_average, "#000000"
    elif (red_average> green_average+blue_average):
      return red_average, "#FF0000"
    else:
      return gray_average, "#000000"

  @staticmethod 
  def create_frame(raw_frame:np.array):
    r,g,b,gray = ImageHelper.split_image(raw_frame)
    #cv2.imshow("Test", gray)
    #cv2.waitKey()
    font = ImageFont.truetype("""C:\\Users\\popme\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Cascadia.ttf""", 15, encoding='utf-8')
    background = np.uint8(np.ones(raw_frame.shape)*255)
    frame = Image.fromarray(background)

    draw = ImageDraw.Draw(frame)

    for i in range(0, background.shape[0], 15):
      for j in range(0, background.shape[1], 12):
        value, color = ImageHelper.get_color(r,g,b,gray, i, j, 15, 12)
        char = selector[int(value)]
        draw.text((j,i), char, color, font)
    cv2Image = np.array(frame)
    result = cv2.cvtColor(cv2Image, cv2.COLOR_RGB2BGR)
    return result
  



if __name__ == "__main__":
    image = cv2.imread("Picture1.png")
    i = ImageHelper.create_frame(image)
    cv2.imwrite("Test.png", i)

