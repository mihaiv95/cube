from OpenGL.GL import glRotatef, glPushMatrix, glPopMatrix, glMatrixMode, GL_MODELVIEW, glMultMatrixf, glColor3f, glLoadMatrixf, glGetFloatv, GL_MODELVIEW_MATRIX, glTranslatef, glLoadIdentity,GL_PROJECTION
from OpenGL.GLU import gluLookAt
from model.identity_mat import identity_mat44


class Cube:
    def __init__(self, edges):
        self._trans_mat = identity_mat44()
        self._rotation_mat = identity_mat44()
        self._edges = edges
        self.tx = 0
        self.ty = 0
        self.tz = 0
        self.rx = 0
        self.ry = 0
        self.rz = 0
        self._old_x = 0
        self._old_y = 0
        self._old_z = 0

    def draw(self):
        glPushMatrix()
        glColor3f(1, 0, 1)
        for edge in self._edges:
            edge.draw_edge()
        glPopMatrix()

    def render(self, local_rot):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        gluLookAt(-2, 2, -6, 0, 0, 0, 0, 1, 0)
        glMultMatrixf(self._trans_mat)
        glMultMatrixf(self._rotation_mat)

        glPushMatrix()
        self.move_x()
        self.move_y()
        self.move_z()
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        if local_rot:
            self.rotate_local()
        else:
            self.rotate_global()
        self._rotation_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

        self.draw()
        glPopMatrix()

    def rotate(self):
        glPushMatrix()
        glLoadMatrixf(self._trans_mat)
        glRotatef(0.5, 0, 1, 0)
        self._trans_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    def move_x(self):
        glLoadMatrixf(self._trans_mat)
        glTranslatef(self.tx, 0, 0)
        self._trans_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def move_y(self):
        glLoadMatrixf(self._trans_mat)
        glTranslatef(0, self.ty, 0)
        self._trans_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def move_z(self):
        glLoadMatrixf(self._trans_mat)
        glTranslatef(0, 0, self.tz)
        self._trans_mat = glGetFloatv(GL_MODELVIEW_MATRIX)

    def rotate_local(self):
        glMultMatrixf(self._rotation_mat)
        glRotatef(self.rx, 1, 0, 0)
        glRotatef(self.ry, 0, 1, 0)

    def rotate_global(self):
        glRotatef(self.rx, 1, 0, 0)
        glRotatef(self.ry, 0, 1, 0)
        glMultMatrixf(self._rotation_mat)

    def stop(self):
        self.tx = 0
        self.ty = 0
        self.tz = 0
        self.ry = 0
        self.rx = 0
        self.rz = 0
