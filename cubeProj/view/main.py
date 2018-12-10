import pygame
from pygame.locals import DOUBLEBUF, OPENGL, FULLSCREEN

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from model.cube import Cube
from model.edge import Edge
from model.square import Square
from model.axis import Axis
from model.camera import Camera
from model.button import Button
from model.identity_mat import identity_mat44
from model.vertex import Vertex

import numpy as np


SCREEN_SIZE = (1440, 900)


axis = Axis()
sq_vert=[
    (-1, 0, -1),
    (1, 0, -1),
    (-1, 0, 1),
    (1, 0, 1),
    ]

sq_edges=[(0,1),
          (0,2),
          (2,3),
          (1,3)]


square = Square(sq_vert, sq_edges, (1,1,0))


bt_list = [Button(750, 50, 50, 1, 'view/test_image.png'),
           Button(690, 50, 50, 2, 'view/test_image.png'),
           Button(750, 110, 50, 3, 'view/test_image.png'),
           Button(690, 110, 50, 4, 'view/test_image.png'),
           Button(750, 170, 50, 5, 'view/test_image.png'),
           Button(690, 170, 50, 6, 'view/test_image.png'),
           Button(750, 230, 50, 7, 'view/test_image.png'),
           Button(690, 230, 50, 8, 'view/test_image.png'),
           Button(750, 290, 50, 9, 'view/test_image.png'),
           Button(690, 290, 50, 10, 'view/test_image.png')
           ]


vertex0 = Vertex(1, -1, -1)
vertex1 = Vertex(1, 1, -1)
vertex2 = Vertex(-1, 1, -1)
vertex3 = Vertex(-1, -1, -1)
vertex4 = Vertex(1, -1, 1)
vertex5 = Vertex(1, 1, 1)
vertex6 = Vertex(-1, -1, 1)
vertex7 = Vertex(-1, 1, 1)


edges = (Edge(vertex0, vertex1),
         Edge(vertex0, vertex3),
         Edge(vertex0, vertex4),
         Edge(vertex2, vertex1),
         Edge(vertex2, vertex3),
         Edge(vertex2, vertex7),
         Edge(vertex6, vertex3),
         Edge(vertex6, vertex4),
         Edge(vertex6, vertex7),
         Edge(vertex5, vertex1),
         Edge(vertex5, vertex4),
         Edge(vertex5, vertex7),
         )

cube = Cube(edges)
camera = Camera()


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40.0, float(width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global but_id
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|OPENGL|FULLSCREEN)
    x, y = screen.get_size()
    print(x,y)
    resize(*SCREEN_SIZE)
    print(glGetString(GL_VERSION))

    # loadTexture()

    # gluLookAt(-1.5, 2, -6, 0, 0, 0, 0, 1, 0)
    for button in bt_list:
        button.load_texture(button._path)
    square.translate()
    # button.rotate2(90,1,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                for button in bt_list:
                    if button.is_pressed(position):
                        if button._id == 1:
                            cube.tx = .1
                        if button._id == 2:
                            cube.tx = -.1
                        if button._id == 3:
                            cube.ty = .1
                        if button._id == 4:
                            cube.ty = -.1
                        if button._id == 5:
                            cube.tz = .1
                        if button._id == 6:
                            cube.tz = -.1
                        if button._id == 7:
                            cube.rx = .5
                        if button._id == 8:
                            cube.rx = -.5
                        if button._id == 9:
                            cube.ry = .5
                        if button._id == 10:
                            cube.ry = -.5

            elif event.type == pygame.MOUSEBUTTONUP:
                cube.stop()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_a:
                    camera.tx = 0.1
                elif event.key == pygame.K_d:
                    camera.tx = -0.1
                elif event.key == pygame.K_w:
                    camera.tz = 0.1
                elif event.key == pygame.K_s:
                    camera.tz = -0.1
                elif event.key == pygame.K_q:
                    camera.ty = .1
                elif event.key == pygame.K_e:
                    camera.ty = -.1
                elif event.key == pygame.K_RIGHT:
                    camera.ry = 1.0
                elif event.key == pygame.K_LEFT:
                    camera.ry = -1.0
                elif event.key == pygame.K_UP:
                    camera.rx = -1.0
                elif event.key == pygame.K_DOWN:
                    camera.rx = 1.0
                elif event.key == pygame.K_z:
                    camera.rz = -1
                elif event.key == pygame.K_x:
                    camera.rz = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and camera.tx > 0:
                    camera.tx = 0
                elif event.key == pygame.K_d and camera.tx < 0:
                    camera.tx = 0
                elif event.key == pygame.K_w and camera.tz > 0:
                    camera.tz = 0
                elif event.key == pygame.K_s and camera.tz < 0:
                    camera.tz = 0
                elif event.key == pygame.K_q and camera.ty > 0:
                    camera.ty = 0.0
                elif event.key == pygame.K_e and camera.ty < 0:
                    camera.ty = 0.0
                elif event.key == pygame.K_RIGHT and camera.ry > 0:
                    camera.ry = 0.0
                elif event.key == pygame.K_LEFT and camera.ry < 0:
                    camera.ry = 0.0
                elif event.key == pygame.K_UP and camera.rx < 0:
                    camera.rx = 0.0
                elif event.key == pygame.K_DOWN and camera.rx > 0:
                    camera.rx = 0.0
                elif event.key == pygame.K_z and camera.rz < 0:
                    camera.rz = 0.0
                elif event.key == pygame.K_x and camera.rz > 0:
                    camera.rz = 0.0

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glEnable(GL_DEPTH_TEST)

        camera.render()

        axis.render()
        cube.render(False)
        glPopMatrix()

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0.0, SCREEN_SIZE[0], SCREEN_SIZE[1], 0.0, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()
        glDisable(GL_CULL_FACE)

        glClear(GL_DEPTH_BUFFER_BIT)

        for button in bt_list:
            button.draw()

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        pygame.display.flip()
        pygame.time.wait(16)


if __name__ == "__main__":
    main()