import numpy as np
from matplotlib import pyplot as plt
from glob import glob

def cwin(filename):
    with open(filename) as f:
        lines = f.readlines()
        dim_finestra = [int(line.strip().split()[0]) for line in lines]
        n_tuple = [int(line.strip().split()[1]) for line in lines]

    title = filename.split('/')[-1]
    plt.figure(figsize=(15, 8))
    plt.grid(True)
    plt.title(f'Analisi di sensitività {title}')
    plt.xlabel('Dimensione finestra')
    plt.ylabel('Numero di tuple')
    plt.scatter(dim_finestra, n_tuple, color='r')
    plt.plot(dim_finestra, n_tuple, color='r')

    plt.show()

for filename in glob('fileFiltrati/Mercury/Nodi/tupleCount/*'):
    cwin(filename)

for filename in glob('fileFiltrati/Mercury/Errori/tupleCount/*'):
    cwin(filename)

for filename in glob('fileFiltrati/BGL/tupleCount/*'):
    cwin(filename)
