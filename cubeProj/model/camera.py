from OpenGL.GL import *
from OpenGL.GLU import gluLookAt

from model.identity_mat import identity_mat44
from model.square import Square


class Camera:
    def __init__(self):
        self._identity_mat = identity_mat44()
        self.tx = 0
        self.ty = 0
        self.tz = 0
        self.ry = 0
        self.rx = 0
        self.rz = 0
        # self.button = Square()

    def rotate_y(self):
        glLoadIdentity()
        glRotatef(self.ry, 0, 1, 0)
        glMultMatrixf(self._identity_mat)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def rotate_x(self):
        glLoadIdentity()
        glRotatef(self.rx, 1, 0, 0)
        glMultMatrixf(self._identity_mat)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def rotate_z(self):
        glLoadIdentity()
        glRotatef(self.rz, 0, 0, 1)
        glMultMatrixf(self._identity_mat)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def translate(self):
        glLoadIdentity()
        glTranslatef(self.tx, self.ty, self.tz)
        glMultMatrixf(self._identity_mat)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def render(self):
        self.translate()
        self.rotate_y()
        self.rotate_x()
        self.rotate_z()





