'''
COMPUTER GRAPHICS LAB ASSIGNMENT 07-1
PROFESSOR : Taesoo Kwon
TA : Jungho Kim
Author :
    Hanyang University
    Department of Computer Science & Engineering
    Gaon Choi(2019009261)
'''


import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# vertex array
gVertexArrayIndexed = None
# index array
gIndexArray = None

gCamAng = 0
gCamHeight = 1.


def key_callback(window, key, scancode, action, mods):
    # Camera Manipulation Shortcut
    global gCamAng, gCamHeight
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_1:
            gCamAng += np.radians(-10)
        elif key == glfw.KEY_3:
            gCamAng += np.radians(10)
        elif key == glfw.KEY_2:
            gCamHeight += 0.1
        elif key == glfw.KEY_W:
            gCamHeight += -0.1


def drawFrame():
    glBegin(GL_LINES)
    # red - x axis
    glColor3ub(255, 0, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([1., 0., 0.]))
    # green - y axis
    glColor3ub(0, 255, 0)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 1., 0.]))
    # blue - z axis
    glColor3ub(0, 0, 255)
    glVertex3fv(np.array([0., 0., 0.]))
    glVertex3fv(np.array([0., 0., 1.]))

    glEnd()


def createVertexAndIndexArrayIndexed():
    # vertex array
    varr = np.array([
        (0, 0, 0),  # v0
        (1.5, 0, 0),  # v1
        (0, 1.5, 0),  # v2
        (0, 0, 1.5)   # v3
    ], "float32")

    # index array
    iarr = np.array([
        (3, 1, 2),
        (3, 0, 2),
        (3, 1, 0),
        (2, 1, 0)
    ])

    return varr, iarr

def render():
    global gCamAng, gCamHeight
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glLoadIdentity()
    gluPerspective(45, 1, 1, 10)
    gluLookAt(5 * np.sin(gCamAng), gCamHeight, 5 * np.cos(gCamAng), 0, 0, 0, 0, 1, 0)

    drawFrame()
    glColor3ub(255, 255, 255)

    # drawTriangularPyramid_glDrawElements()
    drawTriangularPyramid_glDrawElements()

def drawTriangularPyramid_glDrawElements():
    global gVertexArrayIndexed, glIndexArray
    varr = gVertexArrayIndexed
    iarr = gIndexArray
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 3 * varr.itemsize, varr)
    glDrawElements(GL_TRIANGLES, iarr.size, GL_UNSIGNED_INT, iarr)

def main():
    global gVertexArrayIndexed, gIndexArray

    if not glfw.init():
        return
    window = glfw.create_window(480, 480, "2019009261-7-1", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    gVertexArrayIndexed, gIndexArray = createVertexAndIndexArrayIndexed()
    glfw.swap_interval(1)

    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        render()
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()