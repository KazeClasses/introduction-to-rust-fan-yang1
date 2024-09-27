import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("test.text", encoding='utf-16', delimiter=',')
plt.scatter(data[:, 0], data[:, 1])
plt.show()
