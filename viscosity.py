import numpy as np
import matplotlib.pyplot as plt

x = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
y = [0.284, 0.292, 0.305, 0.314, 0.315, 0.313, 0.285]


plt.title("Lab2: Determination of the viscosity of oil\n"
            "\n"
          "Code: https://github.com/javlonbeckk/physicslab/viscosity.py")
plt.plot(x, y, marker="*")
plt.show()