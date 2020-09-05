from moviepy.editor import *
from cv2 import VideoWriter, VideoWriter_fourcc
from image import ImageHelper
import cv2




if __name__ == "__main__":
  clip = VideoFileClip("ProducePandas - Lalala.mp4")
  subClip = clip
  print(clip.size)
  frames = subClip.iter_frames()
  counter = 0
  video = VideoWriter("Tiny.mp4", VideoWriter_fourcc(*'mp4v'), 25, (clip.size[0], clip.size[1]))
  for frame in frames:
    counter+=1
    print(counter, end=' ')
    cv2Frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    f = ImageHelper.create_frame(cv2Frame)
    # print(f.shape)
    video.write(f)
    # cv2.imwrite("Test"+str(counter)+".png", f)
  video.release()
    