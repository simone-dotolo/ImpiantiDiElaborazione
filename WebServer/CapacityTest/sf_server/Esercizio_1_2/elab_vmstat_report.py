import pandas as pd
from matplotlib import pyplot as plt
import glob

# r cpu bottleneck
# b disk bottleneck
# si (swap in) memory bottleneck

stats = ['r', 'b', 'si']

plt.figure(figsize=(15,8))

for (i,stat) in enumerate(stats):

	free_dict = {}

	for file_name in glob.glob('*.txt'):
		
		print(f'\n-----------\nReading {file_name}...')
		f = pd.read_table(file_name, skiprows=1, sep=r"\s+")
		print(f.columns)
		CTT = int((file_name.split('.')[0]).split('_')[2])
		print(f'Constant Throughput Timer: {CTT}.')

		free = f[stat].mean()
		print(f'Free: {free:.2f} seconds.\n-----------\n')
		
		
		if CTT in free_dict.keys():
			free_dict[CTT].append(free)
		else:
			free_dict[CTT] = [free]

	CTT_list = [CTT for CTT in free_dict.keys()]
	CTT_list.sort()

	free_data = [(CTT, sum(free_dict[CTT]) / len(free_dict[CTT])) for CTT in CTT_list]
	free_data.sort(key=lambda x : x[0])
	free_list = [el[1] for el in free_data]

	plt.subplot(3,1,i+1)
	plt.grid(True)
	plt.xlabel('Constant Throughput Timer')
	plt.ylabel(stat)
	plt.plot(CTT_list, free_list)

plt.show()

