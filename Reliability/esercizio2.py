import numpy as np
from matplotlib import pyplot as plt

MTTF = 800
m = 2
s = 4
l = 1/MTTF
t = np.linspace(0,2000,10000)
R = np.array([np.exp(-l*tp) for tp in t])
sys2 = 1-(1-R**s)**m
sys1 = (1-(1-R)**m)**s

plt.figure(figsize=(15,8))

plt.title('System 1 vs System 2')
plt.grid(True)
plt.plot(t, sys1, color='b', label='System 1')
plt.plot(t, sys2, color='r', label='System 2')
plt.xlabel('Time (t)')
plt.ylabel('Reliability R(t)')
plt.ylim(0,1)
plt.xlim(0,2000)
plt.legend()

plt.show()

print(1-(1-np.exp(-l*800)**4)**2)
print((1-(1-(np.exp(-l*800)))**2)**4)
