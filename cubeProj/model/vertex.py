from OpenGL.GL import glVertex3fv, glVertex2fv


class Vertex:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def draw(self):
        if self._z is None:
            glVertex2fv((self._x,self._y))
        else:
            glVertex3fv((self._x,self._y,self._z))