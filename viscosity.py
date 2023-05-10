import numpy as np
import matplotlib.pyplot as plt


def find_viscosity(t, d): # function to find viscosity
    p1 = 0.01135
    p2 = 0.001269
    g = 9.81
    h = 0.33
    v = h / t

    viscosity = (p1-p2) * g * (d**2) / (18 * v)
    return viscosity

# all data
d = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3] # diamaters
t = [6.00, 5.43, 5.05, 4.70, 4.29, 3.90, 3.23] # time

# initialize x and y coordinates
x = d[:]
y = [find_viscosity(t[i], d[i]) for i in range(7)]

plt.title("Lab2: Determination of the viscosity of oil\n"
            "\n"
          "Code: https://github.com/javlonbeckk/physicslab/blob/main/viscosity.py")
plt.plot(x, y, marker="*")
plt.show()
