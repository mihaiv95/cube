import numpy


def identity_mat44():
    return numpy.matrix(numpy.identity(4), copy=False, dtype='float32')
