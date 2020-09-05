from moviepy.editor import *

clip = VideoFileClip("ProducePandas - Lalala.mp4")

frames = clip.iter_frames()

counter = 0

for frame in frames:
  counter+=1
  print(counter, sep=' ')