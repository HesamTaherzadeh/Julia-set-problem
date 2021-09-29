"""
Julia set problem through OOP
"""
import time
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import line_profiler


class JuliaSet:
    """
    given two coords of top (x0, y0)
    and also two coords of below (x1, y1)
    and a complex number c
    The output will be a simple image with an interesting pattern
    """
    @profile
    def __init__(self, x0, y0, x1, y1, c, desired_width, gray=True, max_iteration=300):
        self.p0 = (x0, y0)
        self.p1 = (x1, y1)
        self.c = c
        self.desired_width = desired_width
        self.max_iteration = max_iteration
        self.width = 0
        self.height = 0
        self.gray = gray
        self._canvas()

    @profile
    def _coord_compute(self):
        x_coords = np.linspace(self.p0[0], self.p1[0], int(desired_width)).reshape((1, 1000))
        y_coords = np.linspace(self.p0[0], self.p1[0], int(desired_width)).reshape((1000, 1))

        self.width = x_coords.shape[0]
        self.height = y_coords.shape[0]
        return x_coords + 1j*y_coords

    @profile
    def _actual_compute(self):
        coord_list = self._coord_compute()
        outputlist = np.zeros(coord_list.shape, dtype=int)
        boollist = np.full(coord_list.shape, True, dtype=bool)

        for i in range(self.max_iteration):
            coord_list[boollist] = coord_list[boollist] ** 2 + c

            boollist[np.abs(coord_list) > 2] = False

            outputlist[boollist] = i
        return outputlist

    @profile
    def _canvas(self):
        output_raw = self._actual_compute()
        max_iterations = float(np.max(output_raw))
        if self.gray:
            plt.imshow(output_raw/(max_iterations*255), cmap=mpl.cm.inferno)
            plt.savefig('JuliaSet1.jpeg', format='jpeg')


if __name__ == '__main__':

    x0, x1, y0, y1 = -1.8, 1.8, -1.8, 1.8
    c_real, c_imag = -0.62772, -0.42193
    c = c_real + 1j * c_imag
    desired_width = 1000
    canvas = JuliaSet(x0, y0, x1, y1, c, desired_width,max_iteration=300)






