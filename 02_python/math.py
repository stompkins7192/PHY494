import numpy as np
import matplotlib.pyplot as plt
# Python program to print all
# prime number in an interval
import matplotlib as mpl

a = 1.0
v0 = 0.0
t, h, n = 0.0, 0.1, 20
ta, xa = [], []
for i in range(n):
    x = v0*t + a*t*t / 2.0
    ta.append(t)
    xa.append(x)
    t = t + h

plt.figure(figsize=(4, 4))
plt.plot(ta, xa, '-o', color='red', linewidth=2)
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.savefig("motion.png")
plt.show()
