from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65,1,0.1,50)
    gluLookAt(4,10,7,
              0,0,0,
              0,1,0)

    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

def rectangle(x, y, z, x1, y1, z1, x2, y2, z2, x3, y3, z3, r, g, b, typ):
    glColor(r, g, b)
    glBegin(typ)
    glVertex3d(x, y, z)
    glVertex3d(x1, y1, z1)
    glVertex3d(x2, y2, z2)
    glVertex3d(x3, y3, z3)
    glEnd()


angle=0
forward =True
x=0
z=0
a=0

def arrowkeys(key, x, y):
    global z
    if key == GLUT_KEY_LEFT:
        z-=1
    elif key == GLUT_KEY_RIGHT:
        z+=1
    draw()

def draw():
    global angle
    global x
    global forward
    global z

    global a

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(50, -5, -8,-30, -5, -8,-30, -5, 0,50, -5, 0,0.4, 0.4, 0.4,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(50, -5, -22,-45, -5, -22,-45, -5, -8,50, -5, -8,0.3, 0, 0,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(50, -5, 14,-35, -5, 14,-35, -5, 0,50, -5, 0,0.3, 0, 0,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(50, -5, -22,-45, -5, -22,-45, -5, -50,50, -5, -50,0, 0, 0,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x+4, -5, -3,-x, -5, -3,-x, -5, -2,-x+4, -5, -2,1, 1, 1,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x+4, -5, -5,-x, -5, -5,-x, -5, -4,-x+4, -5, -4,1, 1, 1,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x+12, -5, -5, -x+8, -5, -5, -x+8, -5, -4, -x+12, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x+12, -5, -3,-x+8, -5, -3,-x+8, -5, -2,-x+12, -5, -2,1, 1, 1,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x + 20, -5, -3, -x + 16, -5, -3, -x + 16, -5, -2, -x + 20, -5, -2, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x + 20, -5, -5, -x + 16, -5, -5, -x + 16, -5, -4, -x + 20, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x-8, -5, -3,-x-4, -5, -3,-x-4, -5, -2,-x-8, -5, -2,1, 1, 1,GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x-8, -5, -5, -x-4, -5, -5, -x-4, -5, -4, -x-8, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x-16, -5, -5, -x-12, -5, -5, -x-12, -5, -4, -x-16, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x-16, -5, -3, -x-12, -5, -3, -x-12, -5, -2, -x+-16, -5, -2, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x + 28, -5, -5, -x + 24, -5, -5, -x + 24, -5, -4, -x + 28, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x+28, -5, -3, -x+24, -5, -3, -x+24, -5, -2, -x+28, -5, -2, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x + 36, -5, -5, -x + 32, -5, -5, -x + 32, -5, -4, -x + 36, -5, -4, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    rectangle(-x + 36, -5, -3, -x + 32, -5, -3, -x + 32, -5, -2, -x + 36, -5, -2, 1, 1, 1, GL_POLYGON)

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glRotate(90, 0, 1, 0)
    glTranslate(x, 0, 0 + z)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x, 5*0.25, 0+z)
    glScale(0.5,0.25,0.5)

    glutSolidCube(5)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x+5*0.5,-5*0.25*0.5,5*0.5*0.5+z)

    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125,0.5,12,10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x+5*0.5,-5*0.25*0.5,-5*0.5*0.5+z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x-5*0.5,-5*0.25*0.5,-5*0.5*0.5+z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glTranslate(x-5*0.5,-5*0.25*0.5,5*0.5*0.5+z)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1,0.8,0.2)
    glTranslate(x-8*0.35,0.35,-0.9+z)
    glutWireSphere(0.35,10,8)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(1, 0.8, 0.2)
    glTranslate(x - 8 * 0.35, 0.35, 0.9+z)
    glutWireSphere(0.35, 10, 8)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.6, 0.3, 0)
    glTranslate(-x+10, 0, -8)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.2, 0.6, 0)
    glTranslate(-x + 10, 2.2, -8)
    glutSolidSphere(1.5,10,10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.6, 0.3, 0)
    glTranslate(-x,0,-8)
    glScale(0.08,0.7,0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.2, 0.6, 0)
    glTranslate(-x , 2.2, -8)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)

    glColor3f(0.6, 0.3, 0)
    glTranslate(-x-10, 0, -8)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.2, 0.6, 0)
    glTranslate(-x-10 , 2.2, -8)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.6, 0.3, 0)
    glTranslate(-x +20, 0, -8)
    glScale(0.08, 0.7, 0.08)
    glutSolidCube(5)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.2, 0.6, 0)
    glTranslate(-x + 20, 2.2, -8)
    glutSolidSphere(1.5, 10, 10)

    glLoadIdentity()
    glRotate(90, 0, 1, 0)
    glColor3f(0.2, 0.6, 1)
    glTranslate(a , 2, 0)
    glutSolidSphere(1, 20, 10)

    if forward :

       angle +=0.7
       x +=0.002
       a -=0.01
       if x> 10:
           forward=False
    else:
        angle -= 0.7
        x -= 0.002
        a+=0.01
        if x< -7:
           forward = True

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE |GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"moving car")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(arrowkeys)
myinit()
glutMainLoop()