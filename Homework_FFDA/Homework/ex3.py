import numpy as np
from matplotlib import pyplot as plt
from glob import glob

def rel(filename):
    f = [int(line.strip()) for line in open(filename).readlines()]
    data = np.array(f)

    x, counts = np.unique(data, return_counts=True)
    cusum = np.cumsum(counts)
    empTTF = cusum / cusum[-1]
    empRel = 1 - empTTF

    title = filename.split('/')[-2]
    plt.figure(figsize=(15, 8))
    plt.grid(True)
    plt.title(f'Empirical Reliability vs Empirical TTF ({title})')
    plt.plot(x, empTTF, color='r', label='Empirical TTF') 
    plt.scatter(x, empTTF, s=2, color='r') 
    plt.plot(x, empRel, color='b', label='Empirical Reliability') 
    plt.scatter(x, empRel, s=2, color='b') 
    plt.xlabel('Time (s)')
    plt.ylabel('p')
    plt.xlim(-10e-3)
    plt.ylim(-10e-3,1+10e-3)
    plt.legend()

    plt.show()

    return x, empRel, title

xs = []
empRels = []
labels = []

for filename in glob('tupling_fileFiltrati/BGL/logFiltrati/*'):
    filename += '/interarrivals.txt'
    x, empRel, label = rel(filename)
    xs.append(x)
    empRels.append(empRel)
    labels.append(label)

x, empRel, label = rel('tupling_BGLErrorLog-200/interarrivals.txt')
xs.append(x)
empRels.append(empRel)
labels.append(label)

plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Reliability dei nodi vs Reliability del sistema BGL')
for i in range(len(empRels)):
    plt.plot(xs[i], empRels[i], label=labels[i])
    plt.scatter(xs[i], empRels[i], s=2)
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3)
plt.ylim(-10e-3,1+10e-3)
plt.legend()
plt.show()

xs = []
empRels = []
labels = []

for filename in glob('tupling_fileFiltrati/Mercury/Nodi/logFiltrati/*'):
    filename += '/interarrivals.txt'
    x, empRel, label = rel(filename)
    xs.append(x)
    empRels.append(empRel)
    labels.append(label)

x, empRel, label = rel('tupling_MercuryErrorLog-200/interarrivals.txt')
xs.append(x)
empRels.append(empRel)
labels.append(label)

plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Reliability dei nodi vs Reliability del sistema Mercury')
for i in range(len(empRels)):
    plt.plot(xs[i], empRels[i], label=labels[i])
    plt.scatter(xs[i], empRels[i], s=2)
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3)
plt.ylim(-10e-3,1+10e-3)
plt.legend()
plt.show()