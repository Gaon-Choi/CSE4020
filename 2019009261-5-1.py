'''
COMPUTER GRAPHICS LAB ASSIGNMENT 05-1
PROFESSOR : Taesoo Kwon
TA : Jungho Kim
Author :
    Hanyang University
    Department of Computer Science & Engineering
    Gaon Choi(2019009261)
'''

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def myOrtho(left, right, bottom, top, near, far):
    a = 2 / (right - left)
    b = 2 / (top - bottom)
    c = 2 / -(far - near)

    t_x = -(right + left) / (right - left)
    t_y = -(top + bottom) / (top - bottom)
    t_z = -(far + near) / (far - near)

    glMultMatrixf(np.array([[a, 0, 0, t_x],
                            [0, b, 0, t_y],
                            [0, 0, c, t_z],
                            [0, 0, 0,   1]]).T)

def normalize(vec):
    # normalized_vec = vec / |vec|
    normalized_vec = vec / np.sqrt(vec[0]**2 + vec[1] ** 2 + vec[2] ** 2)
    return normalized_vec

def myLookAt(eye, at, up):
    forward = normalize(eye - at)
    side = normalize(np.cross(up, forward))
    uper = normalize(np.cross(forward, side))

    vec = np.array([-np.dot(eye, side), -np.dot(eye, uper), -np.dot(eye, forward)])
    vec_m = np.array([[side[0]   , side[1]   , side[2]   , vec[0]],
                      [uper[0]   , uper[1]   , uper[2]   , vec[1]],
                      [forward[0], forward[1], forward[2], vec[2]],
                      [0         , 0         , 0         ,      1]])
    glMultMatrixf(vec_m.T)

def drawFrame():
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([1., 0., 0.]))

    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 1., 0.]))

    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 0., 1.]))
    glEnd()

def drawUnitCube():
    glBegin(GL_QUADS)
    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f( 0.5,  0.5,  0.5)

    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f( 0.5, -0.5, -0.5)

    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)

    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glEnd()

def drawCubeArray():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                glPushMatrix()
                glTranslatef(i, j, -k - 1)
                glScalef(.5, .5, .5)
                drawUnitCube()
                glPopMatrix()


def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    myOrtho(-5, 5, -5, 5, -8, 8)
    myLookAt(np.array([5, 3, 5]), np.array([1, 1, -1]), np.array([0, 1, 0]))

    # Above two lines must behave exactly same as the below two lines

    # glOrtho(-5, 5, -5, 5, -8, 8)
    # gluLookAt(5, 3, 5, 1, 1, -1, 0, 1, 0)

    drawFrame()

    glColor3ub(255, 255, 255)
    drawCubeArray()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480, "2019009261-5-1", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
