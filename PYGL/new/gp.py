from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame

 def main():
     pygame.init()
     display=(500,500)
     pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
     
     gluPerspective(40, display[0]display[1],1,10)
     glTranslate(0.0,0.0,-5)

while True:
    
