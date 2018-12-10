from OpenGL.GL import *
from model.vertex import Vertex
class Edge:
    def __init__(self, vertex1, vertex2):
        self._vertex1 = vertex1
        self._vertex2 = vertex2

    def draw_edge(self):
        glLineWidth(2)
        glBegin(GL_LINES)
        self._vertex1.draw()
        self._vertex2.draw()
        glEnd()

    def draw_dotted_edge(self):
        glPushAttrib(GL_ENABLE_BIT)
        glLineStipple(1, 0x1111)
        glEnable(GL_LINE_STIPPLE)
        self.draw_edge()
        glPopAttrib()

