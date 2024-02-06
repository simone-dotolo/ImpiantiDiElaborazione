import pandas as pd
from matplotlib import pyplot as plt
import glob

throughput_dict = {}

for file_name in glob.glob('*.csv'):
	
	print(f'\n-----------\nReading {file_name}...')
	f = pd.read_csv(file_name)
	
	CTT = int((file_name.split('.')[0]).split('_')[2])
	print(f'Constant Throughput Timer: {CTT}.')

	duration = (f['timeStamp'].max() - f['timeStamp'].min()) / 1000.0
	correct_requests = f['success'].value_counts()[True]

	print(f'Duration: {duration:.2f} seconds.')
	print(f'Number of correctly served requests: {correct_requests}.')

	throughput = correct_requests / duration
	print(f'Throughput: {throughput:.2f}.')
	
	if CTT in throughput_dict.keys():
		throughput_dict[CTT].append(throughput)
	else:
		throughput_dict[CTT] = [throughput]

CTT_list = [CTT for CTT in throughput_dict.keys()]
CTT_list.sort()

throughput_data = [(CTT, sum(throughput_dict[CTT]) / len(throughput_dict[CTT])) for CTT in CTT_list]
throughput_data.sort(key=lambda x : x[0])
T_i = [el[1] for el in throughput_data]

O_i = [el / 60.0 for el in CTT_list]

x_i = [t_i / o_i for (t_i, o_i) in zip (T_i, O_i)]

fairness_num = sum(x_i) ** 2
fairness_den = len(O_i) * sum([x**2 for x in x_i])

fairness = fairness_num / fairness_den

print(f'Fairness value: {fairness}')