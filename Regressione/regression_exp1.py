import pandas as pd 
from scipy import stats as st
from matplotlib import pyplot as plt 
import statsmodels.api as sm

df = pd.read_excel('HomeWork_Regression.xls', sheet_name='EXP1')

slope_nmail, intercept_nmail, r_value_nmail, p_value_nmail, std_err_nmail = st.linregress(df['observation'], df['nmail'])
slope_byte_rec, intercept_byte_rec, r_value_byte_rec, p_value_byte_rec, std_err_byte_rec = st.linregress(df['observation'], df['byte rec'])
slope_byte_sent, intercept_byte_sent, r_value_byte_sent, p_value_byte_sent, std_err_byte_sent = st.linregress(df['observation'], df['byte sent'])

plt.figure(figsize=(15,8))

plt.subplot(131)
plt.title(f'nmail | R2: {r_value_nmail**2}')
plt.scatter(df['observation'], df['nmail'], color='b')
plt.plot(df['observation'], df['observation']*slope_nmail + intercept_nmail, color='r')

plt.subplot(132)
plt.title(f'byte rec | R2: {r_value_byte_rec**2}')
plt.scatter(df['observation'], df['byte rec'], color='b')
plt.plot(df['observation'], df['observation']*slope_byte_rec + intercept_byte_rec, color='r')

plt.subplot(133)
plt.title(f'byte sent | R2: {r_value_byte_sent**2}')
plt.scatter(df['observation'], df['byte sent'], color='b')
plt.plot(df['observation'], df['observation']*slope_byte_sent + intercept_byte_sent, color='r')

plt.show()

residui_nmail = df['nmail'] - (df['observation']*slope_nmail + intercept_nmail)
residui_byte_rec = df['byte rec'] - (df['observation']*slope_byte_rec + intercept_byte_rec)
residui_byte_sent = df['byte sent'] - (df['observation']*slope_byte_sent + intercept_byte_sent)

plt.figure(figsize=(15,8))

ax1 = plt.subplot(131)
sm.qqplot(residui_nmail, line='s', ax=ax1)
plt.title(f'QQ-plot nmail')
plt.grid(True)

ax2 = plt.subplot(132)
sm.qqplot(residui_byte_rec, line='s', ax=ax2)
plt.title(f'QQ-plot byte rec')
plt.grid(True)

ax3 = plt.subplot(133)
sm.qqplot(residui_byte_sent, line='s', ax=ax3)
plt.title(f'QQ-plot byte sent')
plt.grid(True)

plt.show()

_, kendall_pvalue_nmail = st.kendalltau(df['observation'], df['nmail'])
_, kendall_pvalue_byte_rec = st.kendalltau(df['observation'], df['byte rec'])
_, kendall_pvalue_byte_sent = st.kendalltau(df['observation'], df['byte sent'])

print(f'Test di Mann-Kendall (nmail), pvalue: {kendall_pvalue_nmail}')
print(f'Test di Mann-Kendall (byte rec), pvalue: {kendall_pvalue_byte_rec}')
print(f'Test di Mann-Kendall (byte sent), pvalue: {kendall_pvalue_byte_sent}')

theils_slope_byte_sent, theils_intercept_byte_sent, theils_low_slope_byte_sent, theils_high_slope_byte_sent = st.theilslopes(df['byte sent'], df['observation'])

print('Regressione Lineare Robusta (Theil e Sen) per byte sent')
print(f'Slope: {theils_slope_byte_sent}')
print(f'Intercept: {theils_intercept_byte_sent}')
print(f'Low Slope: {theils_low_slope_byte_sent}')
print(f'High Slope: {theils_high_slope_byte_sent}')

plt.figure(figsize=(15,8))

plt.title(f'byte sent and robust linear regression')
plt.scatter(df['observation'], df['byte sent'], color='b')
plt.plot(df['observation'], df['observation']*theils_slope_byte_sent + theils_intercept_byte_sent, color='r')
plt.plot(df['observation'], df['observation']*slope_byte_sent + intercept_byte_sent, color='g')

plt.show()