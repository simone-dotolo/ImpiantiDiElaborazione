import numpy as np
from matplotlib import pyplot as plt

##################################### CWIN Mercury
plt.figure(figsize=(15, 8))
plt.title('Analisi di sensitività nodi Mercury (tg-c401 vs tg-c238)')
plt.grid(True)
plt.xlabel('Dimensione finestra')
plt.ylabel('Numero di tuple')
plt.xlim(0,800)

with open('fileFiltrati/Mercury/Nodi/tupleCount/tupleCount-tg-c401.txt') as f:
    lines = f.readlines()
    dim_finestra = [int(line.strip().split()[0]) for line in lines]
    n_tuple = [int(line.strip().split()[1]) for line in lines]
plt.scatter(dim_finestra, n_tuple, color='r')
plt.plot(dim_finestra, n_tuple, color='r', label='tg-c401')

with open('fileFiltrati/Mercury/Nodi/tupleCount/tupleCount-tg-c238.txt') as f:
    lines = f.readlines()
    dim_finestra = [int(line.strip().split()[0]) for line in lines]
    n_tuple = [int(line.strip().split()[1]) for line in lines]
plt.scatter(dim_finestra, n_tuple, color='b')
plt.plot(dim_finestra, n_tuple, color='b', label='tg-c238')

plt.legend()
plt.show()

##################################### Reliability Mercury
plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Confronto Reliability nodi Mercury (tg-c401 vs tg-c238)')
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.ylim(0,1)
plt.xlim(-4*1e4, 4.5*1e6)

f = [int(line.strip()) for line in open('tupling_fileFiltrati/Mercury/Nodi/logFiltrati/tg-c401-220/interarrivals.txt').readlines()]
data = np.array(f)
x, counts = np.unique(data, return_counts=True)
cusum = np.cumsum(counts)
empTTF = cusum / cusum[-1]
empRel = 1 - empTTF
plt.plot(x, empRel, color='r', label='tg-c401') 
plt.scatter(x, empRel, s=2, color='r') 

f = [int(line.strip()) for line in open('tupling_fileFiltrati/Mercury/Nodi/logFiltrati/tg-c238-220/interarrivals.txt').readlines()]
data = np.array(f)
x, counts = np.unique(data, return_counts=True)
cusum = np.cumsum(counts)
empTTF = cusum / cusum[-1]
empRel = 1 - empTTF
plt.plot(x, empRel, color='b', label='tg-c238') 
plt.scatter(x, empRel, s=2, color='b') 

plt.legend()
plt.show()

##################################### CWIN BGL
plt.figure(figsize=(15, 8))
plt.title('Analisi di sensitività nodi BGL (R71-M0-N4 vs R12-M0-N0)')
plt.grid(True)
plt.xlabel('Dimensione finestra')
plt.ylabel('Numero di tuple')
plt.xlim(0,800)

with open('fileFiltrati/BGL/tupleCount/tupleCount-R71-M0-N4.txt') as f:
    lines = f.readlines()
    dim_finestra = [int(line.strip().split()[0]) for line in lines]
    n_tuple = [int(line.strip().split()[1]) for line in lines]
plt.scatter(dim_finestra, n_tuple, color='r')
plt.plot(dim_finestra, n_tuple, color='r', label='R71-M0-N4')

with open('fileFiltrati/BGL/tupleCount/tupleCount-R12-M0-N0.txt') as f:
    lines = f.readlines()
    dim_finestra = [int(line.strip().split()[0]) for line in lines]
    n_tuple = [int(line.strip().split()[1]) for line in lines]
plt.scatter(dim_finestra, n_tuple, color='b')
plt.plot(dim_finestra, n_tuple, color='b', label='R12-M0-N0')

plt.legend()
plt.show()

##################################### Reliability BGL
plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Confronto Reliability nodi BGL (R71-M0-N4 vs R12-M0-N0)')
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-2*1e3, 7*1e5)

f = [int(line.strip()) for line in open('tupling_fileFiltrati/BGL/logFiltrati/R71-M0-N4-280/interarrivals.txt').readlines()]
data = np.array(f)
x, counts = np.unique(data, return_counts=True)
cusum = np.cumsum(counts)
empTTF = cusum / cusum[-1]
empRel = 1 - empTTF
plt.plot(x, empRel, color='r', label='R71-M0-N4') 
plt.scatter(x, empRel, s=2, color='r') 

f = [int(line.strip()) for line in open('tupling_fileFiltrati/BGL/logFiltrati/R12-M0-N0-280/interarrivals.txt').readlines()]
data = np.array(f)
x, counts = np.unique(data, return_counts=True)
cusum = np.cumsum(counts)
empTTF = cusum / cusum[-1]
empRel = 1 - empTTF
plt.plot(x, empRel, color='b', label='R12-M0-N0') 
plt.scatter(x, empRel, s=2, color='b') 

plt.legend()
plt.show()