#JAVLONBEK IBRAGIMOV
import numpy as np
import matplotlib.pyplot as plt
  

#formula
def find_inertia(m, t, n2):
    n1 = 2
    r = 0.125
    g = 9.81
    H = 0.69

    I = (m * (r**2) * (g * (t**2) - 2*H)) / (2*H*(1+n1/n2))
    return I 

# all data
m = [72, 120, 168, 216, 264]
t = [9.6, 5.6, 4.46, 3.6, 3.6]
n2 = [3, 6, 10.55, 13.95, 14.12]

inertias = [find_inertia(m[i], t[i], n2[i]) for i in range(5)]

# initialize x and y coordinates
x = m[:]
y = inertias[:]

plt.title("Moment of Inertia of a Flywheel\n" 
          "Code: https://github.com/javlonbeckk/physicslab_1.git")
plt.plot(x, y, marker="*")
plt.show()

