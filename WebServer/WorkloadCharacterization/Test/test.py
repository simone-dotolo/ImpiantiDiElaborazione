import random

import numpy as np
import pandas as pd
import statsmodels.api as sm 
from matplotlib import pyplot as plt
from scipy.stats import zscore
from scipy import stats
from scipy.stats import ranksums, kstest
from sklearn.decomposition import PCA

n_components = 10

LLc = pd.read_csv('LLc.csv')

# Dropping nominal columns and columns with NaN values
LLc = LLc.select_dtypes(['number']).dropna(axis=1)

# Dropping constant columns
LLc = LLc.drop(columns=LLc.std()[LLc.std() == 0].index)

# Z-score normalizatoin
LLc = LLc.apply(zscore)

# Principal Component Analysis
pca = PCA(n_components=n_components)
pca.fit(LLc)
LLc_transformed = pca.transform(LLc)

LLc_transformed = pd.DataFrame(LLc_transformed, columns=[f'PC_{i}' for i in range(1,n_components+1)])

# --------------------------------

LLpc = pd.read_csv('LLpc.csv')

# Dropping nominal columns and columns with NaN values
LLpc = LLpc.select_dtypes(['number']).dropna(axis=1)

# Dropping constant columns
LLpc = LLpc.drop(columns=LLpc.std()[LLpc.std() == 0].index)

# Z-score normalizatoin
LLpc = LLpc.apply(zscore)

# Principal Component Analysis
pca = PCA(n_components=n_components)
pca.fit(LLpc)
LLpc_transformed = pca.transform(LLpc)

LLpc_transformed = pd.DataFrame(LLpc_transformed, columns=[f'PC_{i}' for i in range(1,n_components+1)])

pc = 1
for (col1, col2) in zip(LLc_transformed.columns, LLc_transformed.columns):

    PC_LLc = LLc_transformed[col1] 
    PC_LLpc = LLpc_transformed[col2]
    
    plt.figure(figsize=(15,8))

    ax1 = plt.subplot(131)
    plt.title(f'QQplot Principal Component {pc} LLc')
    plt.grid(True)
    sm.qqplot(PC_LLc, line='45', ax=ax1)
    
    ax2 = plt.subplot(132)
    plt.title(f'QQplot Principal Component {pc} LLpc')
    plt.grid(True)
    fig = sm.qqplot(PC_LLpc, line='45', ax=ax2)
    
    plt.subplot(133)
    pd.DataFrame([PC_LLc,PC_LLpc]).transpose().boxplot()
    plt.title('Box Plot')
    plt.grid(True)
    
    
    print(f'***************************\nComponente principale {pc}')
    res1 = kstest(PC_LLc, stats.norm.cdf)
    res2 = kstest(PC_LLpc, stats.norm.cdf)
    
    plt.show()

    if min(res1[1], res2[1]) < 0.05:
      print('Non normali. Wilcoxon rank-sum test:')

      _, p = ranksums(PC_LLc, PC_LLpc)
      if p < 0.05:
        print(f'H0 rigettata, p-value: {p}')
      else:
        print(f'H0 non rigettata, p-value: {p}')
    else:
        print('Normali.')

        if pc in [4,5]:
          print('Stessa varianza. Two-sample t-test con varianza uguale:')
          res = stats.ttest_ind(PC_LLc, PC_LLpc, equal_var=True)
        else:
          print('Stessa diversa. Two-sample t-test con varianza diversa:')
          res = stats.ttest_ind(PC_LLc, PC_LLpc, equal_var=False)
        if res[1] < 0.05:
           print(f'H0 rigettata, p-value: {res[1]}')
        else:
           print(f'H0 non rigettata, p-value: {res[1]}')

    pc += 1
