from PIL import Image
from matplotlib.pyplot import plot
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.cm as cm


def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density)) #using linspace to dictate the range of the plotted values as well as the "resolution of each point"
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density)) #The larger the pixel density, less the previous x and y values will increment once they are plotted
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j #this creates the list of all possible solutions where the value returned can be thought of as a two dimensional array

def is_stable(c, num_iterations):
    z = 0 #number of iterations is 20 so there is sufficient testing to see of the result is unbounded
    for _ in range(num_iterations): #vectorization function will iterate through c to determine if the value is not bounded
        z = z ** 2 + c #mandelbrot equation
    return abs(z) <= 2 # generator that will return either true or false for the point that it is located

def julia(c1):
   c = -0.1 +0.65j
   to_plot = np.zeros((300,400))
   for i in range(len(c1)):
    for j in range(len(c1[0])):

        nit = 0
        z = c1[i][j]

        while abs(z) < 10 and nit < 1000:
            z = z **2 + c
            nit += 1
        shade = 1-np.sqrt(nit / 1000)
        ratio = shade / 1000
        to_plot[i][j] = ratio
   return to_plot

c = complex_matrix(-2, 2, -1.5, 1.5, pixel_density=100)


x = julia(c)
print(x)
plt.imshow(x,interpolation='nearest', cmap=cm.hot)
plt.show()
# plt.imshow(is_stable(c, num_iterations=15), cmap="binary")
# #plt.imshow(julia_set(c, num_iterations=15), cmap="binary")
# plt.gca().set_aspect("equal")
# plt.axis("off")
# plt.tight_layout()