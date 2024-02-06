from math import ceil
from matplotlib import pyplot as plt 
import numpy as np
from scipy.stats import shapiro
import pingouin as pg 
from scipy.stats import t, obrientransform, f_oneway, ttest_ind

first_ten_pc_10000 = [3382.8,
                      3981.4,
                      4300.2,
                      4486.2,
                      4377.2,
                      4247.4,
                      4502.8,
                      4692.6,
                      4306,
                      4103.4
                     ]


first_ten_pc_1000000 = [299180.8,
                        302526.8,
                        298758.4,
                        303138.8,
                        302412.8,
                        302406,
                        303688,
                        301799.4,
                        300727.8,
                        304562
                        ]

first_ten_laptop_10000 = [2957.4,
                          3010.8,
                          2473.6,
                          2378.8,
                          2150,
                          2899,
                          2725.8,
                          2822.6,
                          2807.6,
                          2644.6
                         ]

first_ten_laptop_1000000 = [218973.4,
                            223506.6,
                            217941.8,
                            221713.2,
                            222334,
                            218650.6,
                            217433.8,
                            218238.6,
                            222302.6,
                            224741
                           ]

v = [(first_ten_pc_10000, 'PC 10000 bodies'), (first_ten_laptop_10000, 'Laptop 10000 bodies'), (first_ten_pc_1000000, 'PC 1000000 bodies'), (first_ten_laptop_1000000, 'Laptop 1000000 bodies')]

plt.figure(figsize=(15,15))

for (i,el) in enumerate(v):
    el, title = el

    el = np.array(el)
    
    E = 0.1 if i < 2 else 0.01

    # Non-parametric test
    _, pvalue = shapiro(el)
    sample_size = ceil((np.std(el) * 1.96 * 2/ (E*np.mean(el)))**2)

    plt.subplot(2,2,i+1)
    ax = pg.qqplot(el, dist='norm', confidence=.95)
    plt.title(f'{title} | p-value Shapiro: {pvalue} | Sample size: {sample_size}')
    plt.grid(True)

plt.show()

full_sample_pc_10000 = [3382.8,
                        3981.4,
                        4300.2,
                        4486.2,
                        4377.2,
                        4247.4,
                        4502.8,
                        4692.6,
                        4306,
                        4103.4,
                        3698.2
                       ]


full_sample_pc_1000000 = [299180.8,
                          302526.8,
                          298758.4,
                          303138.8,
                          302412.8,
                          302406,
                          303688,
                          301799.4,
                          300727.8,
                          304562
                         ]

full_sample_laptop_10000 = [2957.4,
                            3010.8,
                            2473.6,
                            2378.8,
                            2150,
                            2899,
                            2725.8,
                            2822.6,
                            2807.6,
                            2644.6,
                            3031,
                            2214.4,
                            2204.6,
                            2332,
                            2215.4
                           ]

full_sample_laptop_1000000 = [218973.4,
                              223506.6,
                              217941.8,
                              221713.2,
                              222334,
                              218650.6,
                              217433.8,
                              218238.6,
                              222302.6,
                              224741,
                              218625,
                              218834,
                              222447,
                              223949.8,
                              220169.8,
                              215554.8,
                              223441.8,
                              217705.4,
                              222834.4,
                              223965
                             ]

v = [(full_sample_pc_10000, 'PC 10000 bodies'), (full_sample_laptop_10000, 'Laptop 10000 bodies'), (full_sample_pc_1000000, 'PC 1000000 bodies'), (full_sample_laptop_1000000, 'Laptop 1000000 bodies')]

plt.figure(figsize=(15,15))

for (i,el) in enumerate(v):
    el, title = el

    el = np.array(el)
    
    # Non-parametric test
    _, pvalue = shapiro(el)

    plt.subplot(2,2,i+1)
    ax = pg.qqplot(el, dist='norm', confidence=.95)
    plt.title(f'{title} | p-value Shapiro: {pvalue}')
    plt.grid(True)

plt.show()

cis = []
confidence = 0.95

for sample in v:
    sample, _ = sample
    sample = np.array(sample)
    
    ts = t.interval(confidence, len(sample)-1, loc=0, scale=1 )[1]

    lower = np.mean(sample) - (ts * np.std(sample)) / np.sqrt(len(sample))
    upper = np.mean(sample) + (ts * np.std(sample)) / np.sqrt(len(sample))

    cis.append([lower, upper])

plt.figure(figsize=(15,8))

plt.subplot(121)
plt.title('Intervallo di confidenza 95% (10000 bodies)')
plt.scatter('PC', cis[0][0], color='r')
plt.scatter('PC', cis[0][1], color='r')
plt.vlines('PC', cis[0][0], cis[0][1], color='r')
plt.scatter('Laptop', cis[1][0], color='b')
plt.scatter('Laptop', cis[1][1], color='b')
plt.vlines('Laptop', cis[1][0], cis[1][1], color='b')

plt.subplot(122)
plt.title('Intervallo di confidenza 95% (1000000 bodies)')
plt.scatter('PC', cis[2][0], color='r')
plt.scatter('PC', cis[2][1], color='r')
plt.vlines('PC', cis[2][0], cis[2][1], color='r')
plt.scatter('Laptop', cis[3][0], color='b')
plt.scatter('Laptop', cis[3][1], color='b')
plt.vlines('Laptop', cis[3][0], cis[3][1], color='b')

plt.show()


plt.figure(figsize=(15,8))

tx, ty = obrientransform(full_sample_pc_10000, full_sample_laptop_10000)
_, p = f_oneway(tx, ty)
plt.subplot(121)
plt.title(f'Test di O\'Brien pvalue: {p}')
plt.grid(True)
for point in full_sample_pc_10000:
    plt.scatter('PC', point, color='r')
for point in full_sample_laptop_10000:
    plt.scatter('Laptop', point, color='b')

tx, ty = obrientransform(full_sample_pc_1000000, full_sample_laptop_1000000)
_, p = f_oneway(tx, ty)
plt.subplot(122)
plt.title(f'Test di O\'Brien pvalue: {p}')
plt.grid(True)
for point in full_sample_pc_1000000:
    plt.scatter('PC', point, color='r')
for point in full_sample_laptop_1000000:
    plt.scatter('Laptop', point, color='b')

plt.show()

p_10000 = ttest_ind(full_sample_pc_10000, full_sample_laptop_10000, equal_var=True)[1]
p_1000000 = ttest_ind(full_sample_pc_1000000, full_sample_laptop_1000000, equal_var=True)[1]

print(f'{'*'*10} Two-sample t-test con stessa varianza (10000 bodies) {'*'*10}')
if p_10000 < 0.05:
    print(f'pvalue: {p_10000} | Ipotesi nulla rigettata')
else:
    print(f'pvalue: {p_10000} | Ipotesi nulla non rigettata')

print(f'{'*'*10} Two-sample t-test con stessa varianza (1000000 bodies) {'*'*10}')
if p_1000000 < 0.05:
    print(f'pvalue: {p_1000000} | Ipotesi nulla rigettata')
else:
    print(f'pvalue: {p_1000000} | Ipotesi nulla non rigettata')