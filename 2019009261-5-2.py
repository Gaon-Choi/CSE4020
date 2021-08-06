'''
COMPUTER GRAPHICS LAB ASSIGNMENT 05-2
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

    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)

    glVertex3f( 0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5, -0.5)

    glVertex3f(-0.5,  0.5,  0.5)
    glVertex3f(-0.5,  0.5, -0.5)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5,  0.5)

    glVertex3f( 0.5,  0.5, -0.5)
    glVertex3f( 0.5,  0.5,  0.5)
    glVertex3f( 0.5, -0.5,  0.5)
    glVertex3f( 0.5, -0.5, -0.5)
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

def normalize(vec):
    # normalized_vec = vec / |vec|
    normalized_vec = vec / np.sqrt(vec[0]**2 + vec[1] ** 2 + vec[2] ** 2)
    return normalized_vec

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()

    gluPerspective(45, 1, 1, 10)

    # Replace this call with two glRotatef() calls and
    # one glTranslatef() call
    # gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # By default, OpenGL places a camera
    # at the origin pointing in negative z direction
    glTranslatef(0, 0, -np.sqrt(3 * 3 * 3))

    vec_a = np.array([3, 3, 3])
    vec_b = np.array([3, 3, 0])
    value = np.dot(normalize(vec_a), normalize(vec_b)) / 1
    value = np.arccos(value) * (180 / np.pi)    # approximately 35.264 in deg

    # dot(a, b) = |a||b|cos(theta)
    glRotatef(value, 1, 0, 0)
    glRotatef(-45, 0, 1, 0)

    drawFrame()

    glColor3ub(255, 255, 255)
    drawCubeArray()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480, "2019009261-5-2", None, None)
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
