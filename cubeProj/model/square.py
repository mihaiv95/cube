from OpenGL.GL import *
from model.edge import Edge
from model.identity_mat import *


class Square:

    def __init__(self, vertices, edges, color):

        self._identity_mat = identity_mat44()
        self._vertices = vertices
        self._edges = edges
        self._color = color

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixf(self._identity_mat)
        glColor3f(self._color[0],self._color[1],self._color[2])
        for edge in self._edges:
            Edge.draw_edge(Edge(self._vertices[edge[0]],self._vertices[edge[1]]))
        glPopMatrix()

    def draw_full(self):

        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glMultMatrixf(self._identity_mat)
        glColor3f(self._color[0],self._color[1],self._color[2])
        glBegin(GL_POLYGON)
        glVertex3fv(self._vertices[0])
        glVertex3fv(self._vertices[1])
        glVertex3fv(self._vertices[3])
        glVertex3fv(self._vertices[2])
        glEnd()
        glFlush()
        glPopMatrix()

    def rotate(self):
        glPushMatrix()
        glLoadMatrixf(self._identity_mat)
        glRotatef(0.1,1,0,0)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    def translate(self):
        glPushMatrix()
        glLoadMatrixf(self._identity_mat)
        glTranslatef(0, -2, 0)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    def translate2(self,x,y,z):
        glPushMatrix()
        glLoadMatrixf(self._identity_mat)
        glTranslatef(x,y,z)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    def rotate2(self,ang,x,y,z):
        glPushMatrix()
        glLoadMatrixf(self._identity_mat)
        glRotatef(ang,x, y, z)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()




