from model.edge import Edge
from OpenGL.GL import glPushAttrib,glPopAttrib,GL_ENABLE_BIT,glEnable,glPushMatrix,glMatrixMode, glColor3f, glPopMatrix, glMultMatrixf, GL_MODELVIEW, GL_MODELVIEW_MATRIX, glLoadMatrixf, glRotatef, glGetFloatv, glLineStipple, GL_LINE_STIPPLE
from OpenGL.GLU import gluLookAt
from model.identity_mat import identity_mat44
from model.vertex import Vertex

class Axis:
    def __init__(self):
        self._identity_mat = identity_mat44()
        self._vertices = [Vertex(0, 0, 0),
                          Vertex(-3, 0, 0),
                          Vertex(0, 3, 0),
                          Vertex(0, 0, -3),
                          Vertex(3, 0, 0),
                          Vertex(0, -3, 0),
                          Vertex(0, 0, 3),
                          ]
        self._edges = [(0,1),
                       (0,2),
                       (0,3),
                       (0,4),
                       (0,5),
                       (0,6),
                       ]

    def draw(self):

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        gluLookAt(-2, 2, -6, 0, 0, 0, 0, 1, 0)
        glMultMatrixf(self._identity_mat)
        color = 0
        colors=[(1, 0, 0),
                (1, 1, 0),
                (0, 1, 1),
                (1, 0, 0),
                (1, 1, 0),
                (0, 1, 1)
                ]



        for edge in self._edges:
            glColor3f(colors[color][0],colors[color][1],colors[color][2])
            if color > 2:
                Edge.draw_dotted_edge(Edge(self._vertices[edge[0]], self._vertices[edge[1]]))
            else:
                Edge.draw_edge(Edge(self._vertices[edge[0]], self._vertices[edge[1]]))
            color+=1

        glPopMatrix()

    def rotate(self):
        glPushMatrix()
        glLoadMatrixf(self._identity_mat)
        glRotatef(1,0,1,0)
        self._identity_mat = glGetFloatv(GL_MODELVIEW_MATRIX)
        glPopMatrix()

    def render(self):
        self.draw()