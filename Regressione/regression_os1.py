import pandas as pd 
from scipy import stats as st
from matplotlib import pyplot as plt 
import statsmodels.api as sm

df = pd.read_excel('HomeWork_Regression.xls', sheet_name='os1')

slope_vmsize, intercept_vmsize, r_value_vmsize, p_value_vmsize, std_err_vmsize = st.linregress(df['TIME'], df['LIN1_VmSize'])
slope_vmdata, intercept_vmdata, r_value_vmdata, p_value_vmdata, std_err_vmdata = st.linregress(df['TIME'], df['LIN1_VmData'])
slope_rss, intercept_rss, r_value_rss, p_value_rss, std_err_rss = st.linregress(df['TIME'], df['LIN1_RSS'])
slope_byteletti_io, intercept_byteletti_io, r_value_byteletti_io, p_value_byteletti_io, std_err_byteletti_io = st.linregress(df['TIME'], df['LIN1_byte_letti_I_O'])
slope_byteletti_io1, intercept_byteletti_io1, r_value_byteletti_io1, p_value_byteletti_io1, std_err_byteletti_io1 = st.linregress(df['TIME'], df['LIN1_byte_letti_I_O1'])

plt.figure(figsize=(15,8))

plt.subplot(231)
plt.title(f'VmSize | R2: {r_value_vmsize**2}')
plt.scatter(df['TIME'], df['LIN1_VmSize'], color='b')
plt.plot(df['TIME'], df['TIME']*slope_vmsize + intercept_vmsize, color='r')

plt.subplot(232)
plt.title(f'VmData | R2: {r_value_vmdata**2}')
plt.scatter(df['TIME'], df['LIN1_VmData'], color='b')
plt.plot(df['TIME'], df['TIME']*slope_vmdata + intercept_vmdata, color='r')

plt.subplot(233)
plt.title(f'RSS | R2: {r_value_rss**2}')
plt.scatter(df['TIME'], df['LIN1_RSS'], color='b')
plt.plot(df['TIME'], df['TIME']*slope_rss + intercept_rss, color='r')

plt.subplot(234)
plt.title(f'ByteLetti_IO | R2: {r_value_byteletti_io**2}')
plt.scatter(df['TIME'], df['LIN1_byte_letti_I_O'], color='b')
plt.plot(df['TIME'], df['TIME']*slope_byteletti_io + intercept_byteletti_io, color='r')

plt.subplot(236)
plt.title(f'ByteLetti_IO1 | R2: {r_value_byteletti_io1**2}')
plt.scatter(df['TIME'], df['LIN1_byte_letti_I_O1'], color='b')
plt.plot(df['TIME'], df['TIME']*slope_byteletti_io1 + intercept_byteletti_io1, color='r')

plt.show()

residui_vmsize = df['LIN1_VmSize'] - (df['TIME']*slope_vmsize + intercept_vmsize)
residui_vmdata = df['LIN1_VmData'] - (df['TIME']*slope_vmdata + intercept_vmdata)
residui_rss = df['LIN1_RSS'] - (df['TIME']*slope_rss + intercept_rss)
residui_byteletti_io = df['LIN1_byte_letti_I_O'] - (df['TIME']*slope_byteletti_io + intercept_byteletti_io)
residui_byteletti_io1 = df['LIN1_byte_letti_I_O1'] - (df['TIME']*slope_byteletti_io1 + intercept_byteletti_io1)

plt.figure(figsize=(15,8))

ax1 = plt.subplot(231)
sm.qqplot(residui_vmsize, line='s', ax=ax1)
plt.title(f'QQ-plot VmSize')
plt.grid(True)

ax1 = plt.subplot(232)
sm.qqplot(residui_vmdata, line='s', ax=ax1)
plt.title(f'QQ-plot VmData')
plt.grid(True)

ax1 = plt.subplot(233)
sm.qqplot(residui_rss, line='s', ax=ax1)
plt.title(f'QQ-plot RSS')
plt.grid(True)

ax1 = plt.subplot(234)
sm.qqplot(residui_byteletti_io, line='s', ax=ax1)
plt.title(f'QQ-plot ByteLetti_IO')
plt.grid(True)

ax1 = plt.subplot(236)
sm.qqplot(residui_byteletti_io1, line='s', ax=ax1)
plt.title(f'QQ-plot ByteLetti_IO1')
plt.grid(True)

plt.show()

_, kendall_pvalue_vmsize = st.kendalltau(df['TIME'], df['LIN1_VmSize'])
_, kendall_pvalue_vmdata = st.kendalltau(df['TIME'], df['LIN1_VmData'])
_, kendall_pvalue_rss = st.kendalltau(df['TIME'], df['LIN1_RSS'])
_, kendall_pvalue_byteletti_io = st.kendalltau(df['TIME'], df['LIN1_byte_letti_I_O'])
_, kendall_pvalue_byteletti_io1 = st.kendalltau(df['TIME'], df['LIN1_byte_letti_I_O1'])

print(f'Test di Mann-Kendall (VmSize), pvalue: {kendall_pvalue_vmsize}')
print(f'Test di Mann-Kendall (VmData), pvalue: {kendall_pvalue_vmdata}')
print(f'Test di Mann-Kendall (RSS), pvalue: {kendall_pvalue_rss}')
print(f'Test di Mann-Kendall (ByteLetti_IO), pvalue: {kendall_pvalue_byteletti_io}')
print(f'Test di Mann-Kendall (ByteLetti_IO1), pvalue: {kendall_pvalue_byteletti_io1}')

theils_slope_vmsize, theils_intercept_vmsize, theils_low_slope_vmsize, theils_high_slope_vmsize = st.theilslopes(df['LIN1_VmSize'], df['TIME'])

print('Regressione Lineare Robusta (Theil e Sen) per VmSize')
print(f'Slope: {theils_slope_vmsize}')
print(f'Intercept: {theils_intercept_vmsize}')
print(f'Low Slope: {theils_low_slope_vmsize}')
print(f'High Slope: {theils_high_slope_vmsize}')

theils_slope_vmdata, theils_intercept_vmdata, theils_low_slope_vmdata, theils_high_slope_vmdata = st.theilslopes(df['LIN1_VmData'], df['TIME'])

print('Regressione Lineare Robusta (Theil e Sen) per VmData')
print(f'Slope: {theils_slope_vmdata}')
print(f'Intercept: {theils_intercept_vmdata}')
print(f'Low Slope: {theils_low_slope_vmdata}')
print(f'High Slope: {theils_high_slope_vmdata}')

theils_slope_rss, theils_intercept_rss, theils_low_slope_rss, theils_high_slope_rss = st.theilslopes(df['LIN1_RSS'], df['TIME'])

print('Regressione Lineare Robusta (Theil e Sen) per RSS')
print(f'Slope: {theils_slope_rss}')
print(f'Intercept: {theils_intercept_rss}')
print(f'Low Slope: {theils_low_slope_rss}')
print(f'High Slope: {theils_high_slope_rss}')

theils_slope_byteletti_io, theils_intercept_byteletti_io, theils_low_slope_byteletti_io, theils_high_slope_byteletti_io = st.theilslopes(df['LIN1_byte_letti_I_O'], df['TIME'])

print('Regressione Lineare Robusta (Theil e Sen) per ByteLetti_IO')
print(f'Slope: {theils_slope_byteletti_io}')
print(f'Intercept: {theils_intercept_byteletti_io}')
print(f'Low Slope: {theils_low_slope_byteletti_io}')
print(f'High Slope: {theils_high_slope_byteletti_io}')

plt.figure(figsize=(15,8))

plt.subplot(221)
plt.title(f'VmSize and robust linear regression')
plt.scatter(df['TIME'], df['LIN1_VmSize'], color='b')
plt.plot(df['TIME'], df['TIME']*theils_slope_vmsize + theils_intercept_vmsize, color='r')
plt.plot(df['TIME'], df['TIME']*slope_vmsize + intercept_vmsize, color='g')

plt.subplot(222)
plt.title(f'VmData and robust linear regression')
plt.scatter(df['TIME'], df['LIN1_VmData'], color='b')
plt.plot(df['TIME'], df['TIME']*theils_slope_vmdata + theils_intercept_vmdata, color='r')
plt.plot(df['TIME'], df['TIME']*slope_vmdata + intercept_vmdata, color='g')

plt.subplot(223)
plt.title(f'RSS and robust linear regression')
plt.scatter(df['TIME'], df['LIN1_RSS'], color='b')
plt.plot(df['TIME'], df['TIME']*theils_slope_rss + theils_intercept_rss, color='r')
plt.plot(df['TIME'], df['TIME']*slope_rss + intercept_rss, color='g')

plt.subplot(224)
plt.title(f'ByteLetti_IO and robust linear regression')
plt.scatter(df['TIME'], df['LIN1_byte_letti_I_O'], color='b')
plt.plot(df['TIME'], df['TIME']*theils_slope_byteletti_io + theils_intercept_byteletti_io, color='r')
plt.plot(df['TIME'], df['TIME']*slope_byteletti_io + intercept_byteletti_io, color='g')

plt.show()
