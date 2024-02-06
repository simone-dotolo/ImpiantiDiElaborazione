from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import ks_2samp
from sklearn.metrics import r2_score
import numpy as np

filename = 'sensitivity_analysis/tupleCount-BGLErrorLog.txt'
filename_inter = 'tupling_BGLErrorLog-200/interarrivals.txt'
# --------------------------------------------------------------
filename = 'sensitivity_analysis/tupleCount-MercuryErrorLog.txt'
filename_inter = 'tupling_MercuryErrorLog-200/interarrivals.txt'

with open(filename) as f:
    lines = f.readlines()
    dim_finestra = [int(line.strip().split()[0]) for line in lines]
    n_tuple = [int(line.strip().split()[1]) for line in lines]

plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Analisi di sensitività')
plt.xlabel('Dimensione finestra')
plt.ylabel('Numero di tuple')
plt.scatter(dim_finestra, n_tuple, color='r')
plt.plot(dim_finestra, n_tuple, color='r')

plt.show()

f = [int(line.strip()) for line in open(filename_inter).readlines()]
data = np.array(f)

x, counts = np.unique(data, return_counts=True)
cusum = np.cumsum(counts)
empTTF = cusum / cusum[-1]
empRel = 1 - empTTF

plt.figure(figsize=(15, 8))
plt.grid(True)
plt.title('Empirical Reliability vs Empirical TTF')
plt.plot(x, empTTF, color='r', label='Empirical TTF') 
plt.scatter(x, empTTF, s=2, color='r') 
plt.plot(x, empRel, color='b', label='Empirical Reliability') 
plt.scatter(x, empRel, s=2, color='b') 
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3,300000)
plt.ylim(-10e-3,1+10e-3)
plt.legend()

plt.show()

a_exp, b_exp = curve_fit(lambda t, a, b: a*np.exp(b*t), x, empRel, p0=[1,1e-5])[0]
pvalue_exp = ks_2samp(empRel, a_exp*np.exp(b_exp*x))[1]
r2_exp = r2_score(empRel, a_exp*np.exp(b_exp*x))
print(f'Exponential fit pvalue: {pvalue_exp}')
print(f'Exponential fit R2 score: {r2_exp}')

plt.figure(figsize=(15, 8))

plt.subplot(131)
plt.grid(True)
plt.title('Exponential fit')
plt.scatter(x, empRel, s=2, color='b') 
plt.plot(x, a_exp*np.exp(b_exp*x), color='r', label='Exponential fit')
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3,300000)
plt.ylim(-10e-3,1+10e-3)
plt.legend()

a_hyper, b_hyper, c_hyper, d_hyper = curve_fit(lambda t, a, b, c, d: a*np.exp(b*t) + c*np.exp(d*t), x, empRel, p0=[1,1e-5, 1, 1e-5])[0]
pvalue_hyper = ks_2samp(empRel,  a_hyper*np.exp(b_hyper*x) + c_hyper*np.exp(d_hyper*x))[1]
r2_hyper = r2_score(empRel, a_hyper*np.exp(b_hyper*x) + c_hyper*np.exp(d_hyper*x))
print(f'Hyperexponential fit pvalue: {pvalue_hyper}')
print(f'Hyperexponential fit R2 score: {r2_hyper}')

plt.subplot(132)
plt.grid(True)
plt.title('Hyperexponential fit')
plt.scatter(x, empRel, s=2, color='b') 
plt.plot(x, a_hyper*np.exp(b_hyper*x) + c_hyper*np.exp(d_hyper*x), color='r', label='Hyperexponential fit')
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3,300000)
plt.ylim(-10e-3,1+10e-3)
plt.legend()


a_weibull, b_weibull = curve_fit(lambda t, a, b: np.exp(-b*(t**a)), x, empRel, p0=[1,1e-5])[0]
pvalue_weibull = ks_2samp(empRel, np.exp(-b_weibull*(x**a_weibull)))[1]
r2_weibull = r2_score(empRel, np.exp(-b_weibull*(x**a_weibull)))
print(f'Weibull fit pvalue: {pvalue_weibull}')
print(f'Weibull fit R2 score: {r2_weibull}')

plt.subplot(133)
plt.grid(True)
plt.title('Weibull fit')
plt.scatter(x, empRel, s=2, color='b') 
plt.plot(x, np.exp(-b_weibull*(x**a_weibull)), color='r', label='Weibull fit')
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.xlim(-10e-3,300000)
plt.ylim(-10e-3,1+10e-3)
plt.legend()

plt.show()

# ------------------------
filenames_inter = ['tupling_BGLErrorLog-200/interarrivals.txt', 'tupling_MercuryErrorLog-200/interarrivals.txt']
empRels = []
xs = []

for filename_inter in filenames_inter:
    f = [int(line.strip()) for line in open(filename_inter).readlines()]
    data = np.array(f)

    x, counts = np.unique(data, return_counts=True)
    xs.append(x)
    cusum = np.cumsum(counts)
    empRels.append(1 - cusum / cusum[-1])

plt.figure(figsize=(15, 8))
plt.title('empRel BGL vs empRel Mercury')
plt.grid()
plt.plot(xs[0], empRels[0], color='r', label='empRel BGL')
plt.plot(xs[1], empRels[1], color='b', label='empRel Mercury')
plt.xlim(-10e-3,300000)
plt.ylim(-10e-3,1+10e-3)
plt.xlabel('Time (s)')
plt.ylabel('p')
plt.legend()

plt.show()

MTTF_BGL = np.trapz(empRels[0], xs[0])
MTTF_Mercury = np.trapz(empRels[1], xs[1])

print(f'MTTF BGL: {MTTF_BGL}')
print(f'MTTF Mercury: {MTTF_Mercury}')