'''
COMPUTER GRAPHICS LAB ASSIGNMENT 04-1
PROFESSOR : Taesoo Kwon
TA : Jungho Kim
Author :
    Hanyang University
    Department of Computer Science & Engineering
    Gaon Choi(2019009261)
'''

import glfw
from OpenGL.GL import *
import numpy as np

def render(T):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # draw coordinates
    glBegin(GL_LINES)
    glColor3ub(255, 0, 0)
    glVertex2fv(np.array([0., 0.]))
    glVertex2fv(np.array([1., 0.]))
    glColor3ub(0, 255, 0)
    glVertex2fv(np.array([0., 0.]))
    glVertex2fv(np.array([0., 1.]))
    glEnd()

    # draw triangle
    glBegin(GL_TRIANGLES)
    glColor3ub(255, 255, 255)
    glVertex2fv( (T @ np.array([.0, .5, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.0, .0, 1.]))[:-1] )
    glVertex2fv( (T @ np.array([.5, .0, 1.]))[:-1] )
    glEnd()

def key_callback(window, key, scancode, action, mods):
    global gComposedM
    global newM
    # Translate by -0.1 in x direction w.r.t. global coordinate
    if key == glfw.KEY_Q and action == glfw.PRESS:
        newM = np.array([[1., 0., -0.1],
                         [0., 1., 0.],
                         [0., 0., 1.]])
        gComposedM = newM @ gComposedM

    # Translate by 0.1 in x direction w.r.t. global coordinate
    if key == glfw.KEY_E and action == glfw.PRESS:
        newM = np.array([[1., 0., 0.1],
                         [0., 1., 0.],
                         [0., 0., 1.]])
        gComposedM = newM @ gComposedM

    # Rotate by 10 degrees counterclockwise w.r.t. local coordinate
    if key == glfw.KEY_A and action == glfw.PRESS:
        angle = np.radians(10)
        newM = np.array([[np.cos(angle), -np.sin(angle), 0.],
                         [np.sin(angle), np.cos(angle), 0.],
                         [0., 0., 1.]])
        newM = gComposedM @ newM @ (np.identity(3) @ np.linalg.inv(gComposedM))
        gComposedM = newM @ gComposedM

    # Rotate by 10 degress clockwise w.r.t. local coordinate
    if key == glfw.KEY_D and action == glfw.PRESS:
        angle = np.radians(-10)
        newM = np.array([[np.cos(angle), -np.sin(angle), 0.],
                         [np.sin(angle), np.cos(angle), 0.],
                         [0., 0., 1.]])
        newM = gComposedM @ newM @ (np.identity(3) @ np.linalg.inv(gComposedM))
        gComposedM = newM @ gComposedM

    # Reset the triangle with identity matrix
    if key == glfw.KEY_1 and action == glfw.PRESS:
        gComposedM = newM = np.identity(3)
        gComposedM = newM @ gComposedM

    # Scale by 0.9 times in x direction w.r.t. global coordinate
    if key == glfw.KEY_W and action == glfw.PRESS:
        newM = np.array([[0.9, 0., 0.],
                         [0., 1., 0.],
                         [0., 0., 1.]])
        gComposedM = newM @ gComposedM

    # Rotate by 10 degrees counterclockwise w.r.t. global coordinate
    if key == glfw.KEY_S and action == glfw.PRESS:
        angle = np.radians(10)
        newM = np.array([[np.cos(angle), -np.sin(angle), 0.],
                         [np.sin(angle), np.cos(angle), 0.],
                         [0., 0., 1.]])
        gComposedM = newM @ gComposedM

def main():
    if not glfw.init():
        return
    window = glfw.create_window(480, 480, "2019009261-4-1", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.swap_interval(1)

    global gComposedM
    global newM
    gComposedM = np.identity(3)
    newM = np.identity(3)

    while not glfw.window_should_close(window):
        glfw.set_key_callback(window, key_callback)

        # Poll for and process events
        glfw.poll_events()

        render(gComposedM)
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()
