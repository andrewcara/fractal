import numpy as np

x = np.linspace(1,4,3)

print(x[np.newaxis, :])

x = x[np.newaxis, :] + x[:, np.newaxis] *1j

print(x)







