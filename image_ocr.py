import easyocr

import time

import numpy as np
from PIL import Image, ImageDraw

reader = easyocr.Reader(['ch_tra', 'en'])

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def parse_img_txt(img_array):
  
  start =  time.time()
  
  bounds = reader.readtext(img_array)  # EasyOCR to read text from image
  
  image = Image.fromarray(img_array)
  draw_image = draw_boxes(image, bounds)
  stop = time.time()
  #image = draw_boxes(image, bounds)
  #image.save(file_name)
  text = " ".join([tup[1] for tup in bounds])
  time_cost = stop - start
  return text, time_cost, draw_image




def get_text(image):
    # image: np.array
    img_array = np.array(image)
    text, time_cost, draw_image = parse_img_txt(img_array)
    
    return text, time_cost, draw_image
    
    
    
    
    
    
    