import libs 
import struct
import math
import os 
from libs import Bitmap
from libs import word

#Objet to draw 
img = None

#Constructor 
def glInit():
    return None

#Init FrameBuffer
def glCreateWindow(width, height):
    global img 
    img = Bitmap(width,height) 

#Delete actual image 
def glClear(): 
    img.clear()
#Image area can draw
def glViewPort(x,y,widht, height):
    img.viewPort(x,y,widht, height)

#Get Color 
def glColor(r,g,b):
    img.color(r,g,b)

#Init canvas with new color 
def glClearColor(r,g,b):
    img.clearColor(0,0,0) 

#Get new x,y points 
def glVertex(x,y):
    img.vertex(x,y)

#Show new image 
def glFinish():
    img.writeFile("render.bmp")

def glLoadObj(filename): 
    img.load(filename)

glCreateWindow(1000,800)
glViewPort(0,0,1000,800)
glClear()
glColor(1, 1, 1)
glVertex(0,0)
glLoadObj('chip.obj')
glFinish()