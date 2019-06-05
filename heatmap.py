import os
import numpy as np
import cv2 as cv
from PIL import Image
"""
Credit to:
https://stackoverflow.com/questions/48979219/cv2-composting-2-images-of-differing-size
-Combine Image function

"""
#Making heatmap
def read_input(file_name):
    return "hi"


#Save input file as png
new_extension = ".png"
renamee = "diagram.png"
pre, ext = os.path.splitext(renamee)
os.rename(renamee, pre + new_extension)

#Combine images FIXME: Add scaling

graph = cv.imread("./graph.png")
diagram = cv.imread("./diagram.png")

def changeImageSize(maxWidth,
                    maxHeight,
                    image):

    widthRatio  = maxWidth/image.shape[0]
    heightRatio = maxHeight/image.shape[1]

    newWidth    = int(widthRatio*image.shape[0])
    newHeight   = int(heightRatio*image.shape[1])

    newImage    = cv.resize(image, dsize= (newWidth, newHeight),interpolation=cv.INTER_AREA)
    return newImage
graph = changeImageSize(300,300,graph)
# Blending for different alpha
def combine_images(graph, diagram,start_x, start_y,a):
    foreground, background = graph.copy(), diagram.copy()
    foreground_height, foreground_width = foreground.shape[0], foreground.shape[1]
    background_height, background_width = background.shape[0], background.shape[1]
    if foreground_height + start_y > background_height or foreground_width + start_x > background_width:
        raise ValueError("The foreground image exceeds the background at this location")
    end_x = start_x + foreground_width
    end_y = start_y + foreground_height
    alpha = a

    combined = cv.addWeighted(foreground, alpha, background[start_y:end_y,start_x:end_x,:], 1-alpha,0,background)
    background[start_y:end_y,start_x:end_x,:] = combined
    return background
ranges = [.3, .5, .7]
blended = []
for x in ranges:
    blended.append(combine_images(graph, diagram,300,700,x))
for img in blended:
    cv.imshow('test',img)
    cv.waitKey(3000)
