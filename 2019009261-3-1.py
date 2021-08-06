'''
COMPUTER GRAPHICS LAB ASSIGNMENT 03-1
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

GL_mode = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES,
           GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON]

def render(num):
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_mode[num - 1])

    # B. Use np.linspace() (or np.arrange()), np.cos(), np.sin() to compute the positions of vertices.
    # C. Do not hardcode the position of each vertex.
    # D. The 12 vertices should be specified counterclockwise starting from the vertex on the x-axis.
    degs = np.linspace(0, np.radians(360), vertex_num + 1)
    vertices = np.array([np.cos(degs), np.sin(degs)])

    for i in range(vertex_num):
        glVertex2f(vertices[0][i], vertices[1][i])
    glEnd()

def key_callback(window, key, scancode, action, mods):
    # F. If the keys 1, 2, 3, ... 9, 0 are entered, the primitive type should be changed.
    global num  # a global variable to store the primitive type
    if key == glfw.KEY_1:
        if(action == glfw.PRESS): num = 1
    if key == glfw.KEY_2:
        if(action == glfw.PRESS): num = 2
    if key == glfw.KEY_3:
        if(action == glfw.PRESS): num = 3
    if key == glfw.KEY_4:
        if(action == glfw.PRESS): num = 4
    if key == glfw.KEY_5:
        if(action == glfw.PRESS): num = 5
    if key == glfw.KEY_6:
        if(action == glfw.PRESS): num = 6
    if key == glfw.KEY_7:
        if(action == glfw.PRESS): num = 7
    if key == glfw.KEY_8:
        if(action == glfw.PRESS): num = 8
    if key == glfw.KEY_9:
        if(action == glfw.PRESS): num = 9
    if key == glfw.KEY_0:
        if(action == glfw.PRESS): num = 0

def main():
    if not glfw.init():
        return
    # A. Set the window title to [studentID]-[assignment#]-[prob#] (e.g. 2017123456-3-1)
    # and the window size to (480, 480).
    window = glfw.create_window(480, 480, "2019009261-3-1", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    global num
    num = 4
    global vertex_num
    vertex_num = 12

    while not glfw.window_should_close(window):
        glfw.set_key_callback(window, key_callback)
        glfw.poll_events()
        render(num)
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__ == "__main__":
    main()