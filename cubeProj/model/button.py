import pygame.image
from OpenGL.GL import *

from model.identity_mat import identity_mat44
from model.vertex import Vertex


class Button:

    def __init__(self, x, y, dim, id, path):
        self._identity_mat = identity_mat44()
        self._x = x
        self._y = y
        self._v1 = Vertex(x-dim/2, y-dim/2, None)
        self._v2 = Vertex(x+dim/2, y-dim/2, None)
        self._v3 = Vertex(x+dim/2, y+dim/2, None)
        self._v4 = Vertex(x-dim/2, y+dim/2, None)
        self._id = id
        self._path = path
        self._texId = None

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixf(self._identity_mat)
        glColor3f(1,1,1)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self._texId)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0)
        self._v1.draw()
        glTexCoord2f(1.0, 1.0)
        self._v2.draw()
        glTexCoord2f(1.0, 0.0)
        self._v3.draw()
        glTexCoord2f(0.0, 0.0)
        self._v4.draw()
        glEnd()
        glDisable(GL_TEXTURE_2D)
        glFlush()
        glPopMatrix()

    def load_texture(self, path):
        textureSurface = pygame.image.load(path)
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()

        texid = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        self._texId = texid

    def is_pressed(self, pos):
        if (pos[0]>self._v1._x) and (pos[0]<self._v2._x) and (pos[1]<self._v3._y) and (pos[1]>self._v1._y):
            return True
        return False

    def __str__(self):
        return "Button"+str(self._id)