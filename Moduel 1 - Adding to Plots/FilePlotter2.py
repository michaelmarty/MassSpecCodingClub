import numpy as np
import matplotlib.pyplot as plt


def predicted_mz(mass, zrange=[15, 30], adductmass=1):
    zarray = np.arange(zrange[0], zrange[1] + 1)
    mz = (mass + zarray * adductmass) / zarray
    mz = np.round(mz, 0)
    return mz, zarray


path = "C:\\Users\\Teaching\\Desktop\\SPECTRUM - MS.txt"
path = "C:\\Python\\MassSpecCodingClub\\Module 0 - Plotting a Spectrum\\SPECTRUM - MS.txt"

data = np.loadtxt(path, skiprows=8)

x = data[:, 0]
y = data[:, 1]

ymax = np.amax(y)

y = y / ymax * 100

mzrange = [5000, 7000]

mz_vals, zvals = predicted_mz(147500, zrange=[1, 1000])

plt.plot(x, y)
plt.xlim(mzrange[0], mzrange[1])
# plt.plot(mz_vals, np.ones_like(mz_vals)*100, marker="o", linestyle=" ")
for i, mz in enumerate(mz_vals):
    if mz < mzrange[1] and mz > mzrange[0]:
        plt.vlines(mz, 0, 100, linestyles="--", color="black")
        z = zvals[i]
        print(i, mz, z)
        plt.text(mz - 75, 101, "+" + str(z))
        # print(z)

plt.xlabel("m/z")
plt.ylabel("Intensity (%)")

# plt.text(2000, 20, "Monomer")

plt.savefig("testspectrum.png")
plt.show()
