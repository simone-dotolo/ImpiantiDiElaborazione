import glob
import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm 
from matplotlib import pyplot as plt
from scipy import stats

pd.set_option('display.float_format', lambda x: '%.3f' % x)

doe_plan = pd.DataFrame(columns=['Risorsa', 'Intensità', 'Ripetizione', 'Response Time'])

for filename in glob.glob('sf_client/*'):
    print(f'\n-----------\nReading {filename}...')
	
    f = pd.read_csv(filename, on_bad_lines='skip')

    risorsa, ctt, ripetizione = filename.split('/')[1].split('_')
    ctt = int(ctt)
    response_time = f['elapsed'].mean()

    doe_plan.loc[len(doe_plan)] = [risorsa, ctt, ripetizione, response_time]

doe_plan = doe_plan.sort_values(by=['Risorsa', 'Intensità', 'Ripetizione'], ascending=[False, True, True])

print(doe_plan)

a_levels = 3
b_levels = 3
repetition = 5

mu = doe_plan['Response Time'].mean()

a_small = doe_plan.loc[doe_plan['Risorsa'] == 'Small']['Response Time'].mean() - mu
a_medium = doe_plan.loc[doe_plan['Risorsa'] == 'Medium']['Response Time'].mean() - mu
a_large = doe_plan.loc[doe_plan['Risorsa'] == 'Large']['Response Time'].mean() - mu

a = [a_small, a_medium, a_large]

b_950 = doe_plan.loc[doe_plan['Intensità'] == 950]['Response Time'].mean() - mu
b_1900 = doe_plan.loc[doe_plan['Intensità'] == 1900]['Response Time'].mean() - mu
b_2850 = doe_plan.loc[doe_plan['Intensità'] == 2850]['Response Time'].mean() - mu

b = [b_950, b_1900, b_2850]

g_small_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 950)]['Response Time'].mean() - mu - a_small - b_950
g_medium_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 950)]['Response Time'].mean() - mu - a_medium - b_950
g_large_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 950)]['Response Time'].mean() - mu - a_large - b_950
g_small_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 1900)]['Response Time'].mean() - mu - a_small - b_1900
g_medium_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 1900)]['Response Time'].mean() - mu - a_medium - b_1900
g_large_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 1900)]['Response Time'].mean() - mu - a_large - b_1900
g_small_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 2850)]['Response Time'].mean() - mu - a_small - b_2850
g_medium_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 2850)]['Response Time'].mean() - mu - a_medium - b_2850
g_large_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 2850)]['Response Time'].mean() - mu - a_large - b_2850

g = [g_small_950, g_medium_950, g_large_950, g_small_1900, g_medium_1900, g_large_1900, g_small_2850, g_medium_2850, g_large_2850]

y_small_950 = mu + a_small + b_950 + g_small_950
y_medium_950 = mu + a_medium + b_950 + g_medium_950
y_large_950 = mu + a_large + b_950 + g_large_950
y_small_1900 = mu + a_small + b_1900 + g_small_1900
y_medium_1900 = mu + a_medium + b_1900 + g_medium_1900
y_large_1900 = mu + a_large + b_1900 + g_large_1900
y_small_2850 = mu + a_small + b_2850 + g_small_2850
y_medium_2850 = mu + a_medium + b_2850 + g_medium_2850
y_large_2850 = mu + a_large + b_2850 + g_large_2850

y = [y_small_950, y_medium_950, y_large_950, y_small_1900, y_medium_1900, y_large_1900, y_small_2850, y_medium_2850, y_large_2850]

e_small_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 950)]['Response Time'].subtract(y_small_950)
e_medium_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 950)]['Response Time'].subtract(y_medium_950)
e_large_950 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 950)]['Response Time'].subtract(y_large_950)
e_small_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 1900)]['Response Time'].subtract(y_small_1900)
e_medium_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 1900)]['Response Time'].subtract(y_medium_1900)
e_large_1900 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 1900)]['Response Time'].subtract(y_large_1900)
e_small_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 2850)]['Response Time'].subtract(y_small_2850)
e_medium_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 2850)]['Response Time'].subtract(y_medium_2850)
e_large_2850 = doe_plan.loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 2850)]['Response Time'].subtract(y_large_2850)

e = [e_small_950, e_medium_950, e_large_950, e_small_1900, e_medium_1900, e_large_1900, e_small_2850, e_medium_2850, e_large_2850]

# A: Risorsa
# B: Intensità

SSY = sum(y_ijk**2 for y_ijk in doe_plan['Response Time'])
SS0 = a_levels*b_levels*repetition*(mu**2)
SS_risorsa = b_levels*repetition*sum([a_j**2 for a_j in a])
SS_intensità = a_levels*repetition*sum([b_i**2 for b_i in b])
SS_risorsa_intensità = repetition*sum([g_ij**2 for g_ij in g])
SSE = sum([sum([e_ijr**2 for e_ijr in e_ij]) for e_ij in e])

print(f'SSY: {SSY:.3f}')
print(f'SS0: {SS0:.3f}')
print(f'SS_risorsa: {SS_risorsa:.3f}')
print(f'SSB: {SS_intensità:.3f}')
print(f'SSAB: {SS_risorsa_intensità:.3f}')
print(f'SSE: {SSE:.3f}')
print(f'(SSY) {SSY:.3f} = {(SS0+SS_risorsa+SS_intensità+SS_risorsa_intensità+SSE):.3f} (SS0+SS_risorsa+SS_intensità+SS_risorsa_intensità+SSE)')

SST = SSY - SS0
Importance_risorsa = SS_risorsa/SST
Importance_intensità = SS_intensità/SST
Importance_risorsa_intensità = SS_risorsa_intensità/SST
Importance_error = SSE/SST

print(f'Importance_risorsa: {Importance_risorsa}\nImportance_intensità: {Importance_intensità}\nImportance_risorsa_intensità: {Importance_risorsa_intensità}\nImportance_error: {Importance_error}')

res = pd.DataFrame(columns=['Origine', 'DF', 'SS', 'Importanza'])

res.loc[len(res)] = ['Modello', 44, SST, 1]
res.loc[len(res)] = ['Errore', 36, SSE, Importance_error]
res.loc[len(res)] = ['Risorsa', 2, SS_risorsa, Importance_risorsa]
res.loc[len(res)] = ['Intensità', 2, SS_intensità, Importance_intensità]
res.loc[len(res)] = ['IntensitàxRisorsa', 4, SS_risorsa_intensità, Importance_risorsa_intensità]
res = res.set_index('Origine')

print(res)

errors = pd.Series()

for el1 in e:
    for el2 in el1:
        errors.loc[len(errors)] = el2

print(errors)

plt.figure(figsize=(15,8))

ax1 = plt.subplot(121)
errors.plot(kind='hist', ax=ax1)
plt.grid(True)

ax2 = plt.subplot(122)
plt.grid(True)
fig = sm.qqplot(errors, line='s', ax=ax2)
plt.show()

_, p_value = stats.shapiro(errors)

print(f'Shapiro-Wilk test p-value: {p_value}')

doe_plan['Residui'] = 0

doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 950)] = e_small_950
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 950)] = e_medium_950
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 950)] = e_large_950
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 1900)] = e_small_1900
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 1900)] = e_medium_1900
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 1900)] = e_large_1900
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == 2850)] = e_small_2850
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == 2850)] = e_medium_2850
doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == 2850)] = e_large_2850

print(doe_plan)

ctts = doe_plan['Intensità'].unique()
risorse = doe_plan['Risorsa'].unique()

plt.figure(figsize=(15, 8))
plt.subplot(121)
plt.grid(True)
plt.ylabel('Residui')
plt.xlabel('Dimensione Risorsa')
for ctt in ctts:
    small = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Small') & (doe_plan['Intensità'] == ctt)]
    medium = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Medium') & (doe_plan['Intensità'] == ctt)]
    large = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Large') & (doe_plan['Intensità'] == ctt)]
    for smallp, mediump, largep in zip(small, medium, large):
        plt.scatter(['Small', 'Medium', 'Large'], [smallp, mediump, largep])
    
plt.subplot(122)
plt.grid(True)
plt.ylabel('Residui')
plt.xlabel('Intensità')
for risorsa in risorse:
    ctt_950 = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == risorsa) & (doe_plan['Intensità'] == 950)]
    ctt_1900 = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == risorsa) & (doe_plan['Intensità'] == 1900)]
    ctt_2850 = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == risorsa) & (doe_plan['Intensità'] == 2850)]
    for ctt_950p, ctt_1900p, ctt_2850p in zip(ctt_950, ctt_1900, ctt_2850):
        plt.scatter(['950', '1900', '2850'], [ctt_950p, ctt_1900p, ctt_2850p])

plt.show()

small = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Small')]
medium = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Medium')]
large = doe_plan['Residui'].loc[(doe_plan['Risorsa'] == 'Large')]

small, medium, large = stats.obrientransform(small, medium, large)
_, p_value = stats.f_oneway(small, medium, large)
print(f'O\'Brien test per Risorsa, p-value: {p_value}')

ctt_950, ctt_1900, ctt_2850 = stats.obrientransform(ctt_950, ctt_1900, ctt_2850)
_, p_value = stats.f_oneway(ctt_950, ctt_1900, ctt_2850)
print(f'O\'Brien test per Intensità, p-value: {p_value}')

_, p_value = stats.kruskal(doe_plan['Response Time'].loc[(doe_plan['Risorsa'] == 'Small')],
                           doe_plan['Response Time'].loc[(doe_plan['Risorsa'] == 'Medium')],
                           doe_plan['Response Time'].loc[(doe_plan['Risorsa'] == 'Large')],
                           doe_plan['Response Time'])
print(f'Kruskal-Wallis test per Risorsa, p-value: {p_value}')

_, p_value = stats.kruskal(doe_plan['Response Time'].loc[(doe_plan['Intensità'] == 950)],
                           doe_plan['Response Time'].loc[(doe_plan['Intensità'] == 1900)],
                           doe_plan['Response Time'].loc[(doe_plan['Intensità'] == 2850)],
                           doe_plan['Response Time'])
print(f'Kruskal-Wallis test per Intensità, p-value: {p_value}')