from PIL import Image
from matplotlib.pyplot import plot
import numpy as np
import matplotlib.pyplot as plt
import math


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density)) #using linspace to dictate the range of the plotted values as well as the "resolution of each point"
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density)) #The larger the pixel density, less the previous x and y values will increment once they are plotted
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j #this creates the list of all possible solutions where the value returned can be thought of as a two dimensional array

def is_stable(c, num_iterations):
    z = 0 #number of iterations is 20 so there is sufficient testing to see of the result is unbounded
    for _ in range(num_iterations): #vectorization function will iterate through every value in c
        z = z ** 2 + c #mandelbrot equation
    return abs(z) <= 2 # generator that will return either true or false for the point that it is located


c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=600)

print(c)

plt.imshow(is_stable(c, num_iterations=15), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()