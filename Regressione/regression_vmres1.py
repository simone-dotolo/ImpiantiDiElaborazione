import pandas as pd 
from scipy import stats as st
from matplotlib import pyplot as plt 
import statsmodels.api as sm

df = pd.read_excel('HomeWork_Regression.xls', sheet_name='VMres1').dropna()

slope_heap, intercept_heap, r_value_heap, p_value_heap, std_err_heap = st.linregress(df['T(s)'], df['Allocated Heap'])

plt.figure(figsize=(15,8))

plt.title(f'Allocated Heap | R2: {r_value_heap**2}')
plt.scatter(df['T(s)'], df['Allocated Heap'], color='b')
plt.plot(df['T(s)'], df['T(s)']*slope_heap + intercept_heap, color='r')

plt.show()

residui_heap = df['Allocated Heap'] - (df['T(s)']*slope_heap + intercept_heap)

sm.qqplot(residui_heap, line='s')
plt.title(f'QQ-plot Allocated Heap')
plt.grid(True)

plt.show()

_, kendall_pvalue_heap = st.kendalltau(df['T(s)'], df['Allocated Heap'])

print(f'Test di Mann-Kendall (Allocated Heap), pvalue: {kendall_pvalue_heap}')


theils_slope_heap, theils_intercept_heap, theils_low_slope_heap, theils_high_slope_heap = st.theilslopes(df['Allocated Heap'], df['T(s)'])

print('Regressione Lineare Robusta (Theil e Sen) per Allocated Heap')
print(f'Slope: {theils_slope_heap}')
print(f'Intercept: {theils_intercept_heap}')
print(f'Low Slope: {theils_low_slope_heap}')
print(f'High Slope: {theils_high_slope_heap}')

plt.figure(figsize=(15,8))

plt.title(f'Allocated Heap and robust linear regression')
plt.scatter(df['T(s)'], df['Allocated Heap'], color='b')
plt.plot(df['T(s)'], df['T(s)']*theils_slope_heap + theils_intercept_heap, color='r')
plt.plot(df['T(s)'], df['T(s)']*slope_heap + intercept_heap, color='g')

plt.show()
