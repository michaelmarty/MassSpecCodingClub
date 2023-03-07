import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\Teaching\\Desktop\\SPECTRUM - MS.txt"

data = np.loadtxt(path, skiprows=8)

x = data[:,0]
y = data[:,1]

ymax = np.amax(y)

y = y / ymax * 100

plt.plot(x, y)
plt.xlabel("m/z")
plt.ylabel("Intensity (%)")
plt.savefig("testspectrum.png")
plt.show()
