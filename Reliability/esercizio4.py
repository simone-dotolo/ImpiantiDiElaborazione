import numpy as np
from matplotlib import pyplot as plt

MTTFA = 500
MTTFB = 9000
MTTFC = 10000

t = np.linspace(0, 2000, 10000)

RA = np.exp(-t/MTTFA)
RB = np.exp(-t/MTTFB)
RC = np.exp(-t/MTTFC)

# 1
sys1 = 1-(1-RA*RB)*(1-RA*RC)
sys2 = RA*(1-(1-RB)*(1-RC))

plt.figure(figsize=(15,8))
plt.title('1) System1 vs System2')
plt.grid(True)
plt.plot(t, sys1, color='b', label='System 1')
plt.plot(t, sys2, color='r', label='System 2')
plt.ylim(0, 1)
plt.xlim(0)
plt.legend()

plt.show()

# 2
sys1 = RA*(1-(1-RA)*(1-RB))
sys2 = RA

plt.figure(figsize=(15,8))
plt.title('2) System1 vs System2')
plt.grid(True)
plt.plot(t, sys1, color='b', label='System 1')
plt.plot(t, sys2, color='r', label='System 2')
plt.ylim(0, 1)
plt.xlim(0)
plt.legend()

plt.show()

# 3
sys1 = RA*RB*(1-(1-RA)*(1-RB))
sys2 = RA*RB

plt.figure(figsize=(15,8))
plt.title('3) System1 vs System2')
plt.grid(True)
plt.plot(t, sys1, color='b', label='System 1')
plt.plot(t, sys2, color='r', label='System 2')
plt.ylim(0, 1)
plt.xlim(0)
plt.legend()

plt.show()

# 4
sys1 = 1-(1-RA)*(1-RA*RB)
sys2 = RA

plt.figure(figsize=(15,8))
plt.title('4) System1 vs System2')
plt.grid(True)
plt.plot(t, sys1, color='b', label='System 1')
plt.plot(t, sys2, color='r', label='System 2')
plt.ylim(0, 1)
plt.xlim(0)
plt.legend()

plt.show()