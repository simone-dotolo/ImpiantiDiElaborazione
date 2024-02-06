import numpy as np
import matplotlib.pyplot as plt
'''
	Cosa dice il CENTRAL LIMIT THEOREM?????
	Data una qualsiasi popolazione, estraendo un random sample (osservazioni iid) con un numero di osservazioni sufficientemente grande (n > 30, 40 ma non è vero in realtà), e facendo la media delle osservazioni, questa media può essere vista come un'osservazione di una variabile aleatoria normale, indipendentemente dalla distribuzione della popolazione di partenza

'''
def clt(n=10):

	samples_uniform = []
	samples_rayleigh = []
	for i in range(10000):
		samples_uniform.append(np.random.uniform(size=n))
		samples_rayleigh.append(np.random.rayleigh(size=n))
	samples_uniform_mean = [np.mean(sample) for sample in samples_uniform]
	samples_rayleigh_mean = [np.mean(sample) for sample in samples_rayleigh]
	
	hist_uniform_1, bins_uniform_1 = np.histogram([np.mean(sample) for sample in [np.random.uniform(size=1) for i in range(10000)]])
	hist_rayleigh_1, bins_rayleigh_1 = np.histogram([np.mean(sample) for sample in [np.random.rayleigh(size=1) for i in range(10000)]])
	
	hist_uniform, bins_uniform = np.histogram(samples_uniform_mean)
	hist_rayleigh, bins_rayleigh = np.histogram(samples_rayleigh_mean)
	
	plt.figure(figsize=(15, 8))
	
	plt.suptitle('Central Limit Theorem', fontsize=16)

	plt.subplot(221)
	plt.title('Uniform population')
	plt.grid(True)
	plt.hist(bins_uniform_1[:-1], bins_uniform_1, weights=hist_uniform_1)

	plt.subplot(222)
	plt.title('Rayleigh population')
	plt.grid(True)
	plt.hist(bins_rayleigh_1[:-1], bins_rayleigh_1, weights=hist_rayleigh_1)

	plt.subplot(223)
	plt.title(f'Histogram of means from uniform population, samples size n = {n}')
	plt.grid(True)
	plt.hist(bins_uniform[:-1], bins_uniform, weights=hist_uniform)

	plt.subplot(224)
	plt.title(f'Histogram of means from rayleigh population, samples size n = {n}')
	plt.grid(True)
	plt.hist(bins_rayleigh[:-1], bins_rayleigh, weights=hist_rayleigh)

	plt.show()

clt(n=100)
