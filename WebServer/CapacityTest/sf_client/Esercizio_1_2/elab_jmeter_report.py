import pandas as pd
from matplotlib import pyplot as plt
import glob

throughput_dict = {}
responsetime_dict = {}

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

	response_time = f['elapsed'].mean()
	print(f'Response time: {response_time:.2f} seconds.\n-----------\n')
	
	if CTT in throughput_dict.keys():
		throughput_dict[CTT].append(throughput)
	else:
		throughput_dict[CTT] = [throughput]
	
	if CTT in responsetime_dict.keys():
		responsetime_dict[CTT].append(response_time)
	else:
		responsetime_dict[CTT] = [response_time]

CTT_list = [CTT for CTT in throughput_dict.keys()]
CTT_list.sort()

throughput_data = [(CTT, sum(throughput_dict[CTT]) / len(throughput_dict[CTT])) for CTT in CTT_list]
throughput_data.sort(key=lambda x : x[0])
throughput_list = [el[1] for el in throughput_data]

responsetime_data = [(CTT, sum(responsetime_dict[CTT]) / len(responsetime_dict[CTT])) for CTT in CTT_list]
responsetime_data.sort(key=lambda x : x[0])
responsetime_list = [el[1] for el in responsetime_data]

plt.figure(figsize=(15,8))

plt.subplot(311)
plt.grid(True)
plt.xlabel('Constant Throughput Time')
plt.ylabel('Throughput')
plt.plot(CTT_list, throughput_list)
plt.axvline(x=2750.0, color='0.5', linestyle='dashed')
plt.axvline(x=3750.0, color='0.5', linestyle='dashed')

plt.subplot(312)
plt.grid(True)
plt.xlabel('Constant Throughput Time')
plt.ylabel('Response Time')
plt.plot(CTT_list, responsetime_list, color='r')
plt.axvline(x=2750.0, color='0.5', linestyle='dashed')
plt.axvline(x=3750.0, color='0.5', linestyle='dashed')

plt.subplot(313)
plt.grid(True)
plt.xlabel('Constant Throughput Time')
plt.ylabel('Power')
plt.plot(CTT_list, [throughput/responsetime for (throughput, responsetime) in zip(throughput_list, responsetime_list)], color='g')
plt.axvline(x=2750.0, color='0.5', linestyle='dashed')
plt.axvline(x=3750.0, color='0.5', linestyle='dashed')

plt.show()

'''
print(pd.DataFrame(throughput_dict).transpose())
print(throughput_data)


print(pd.DataFrame(responsetime_dict).transpose())
print(responsetime_data)

import numpy as np

print([np.std(responsetime_dict[CTT]) / np.mean(responsetime_dict[CTT]) for CTT in CTT_list])
tmp = [[round(el[1] / el[0],7) for el in zip(responsetime_dict[CTT], throughput_dict[CTT])] for CTT in CTT_list]
print([round(np.mean(el),7) for el in tmp])
'''