import numpy as np
from matplotlib import pyplot as plt

l = 0.005
t = np.linspace(0, 2000, 10000)
R = np.array([np.exp(-l*ts) for ts in t])
sys = R**8 + 8*R**7*(1-R) + 20*R**6*(1-R)**2 + 16*R**5*(1-R)**3 + 2*R**4*(1-R)**4

plt.figure(figsize=(15,8))
plt.xlabel('Time (t)')
plt.ylabel('Reliability R(t)')
plt.grid(True)
plt.plot(t, sys, color='r')

plt.show()

R = np.exp(-l*48)
sys_48 = R**8 + 8*R**7*(1-R) + 20*R**6*(1-R)**2 + 16*R**5*(1-R)**3 + 2*R**4*(1-R)**4
print(sys_48)
