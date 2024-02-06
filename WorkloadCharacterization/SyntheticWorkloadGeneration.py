import random

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import zscore
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

def plot_dendrogram(model, **kwargs):
    from scipy.cluster.hierarchy import dendrogram

    # Children of hierarchical clustering
    children = model.children_

    # Distances between each pair of children
    # Since we don't have this information, we can use a uniform one for plotting
    distance = np.arange(children.shape[0])

    # The number of observations contained in each cluster level
    no_of_observations = np.arange(2, children.shape[0]+2)

    # Create linkage matrix and then plot the dendrogram
    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)

# Selezionare prima n_components pari al numero di colonne per visualizzare quante componenti prendere
# Successivamente n_clusters pari al numero di righe per selezionare il numero corretto di cluster

n_components = 6
n_clusters = 9

f = pd.read_excel('EsercizioPCA_CLustering_vers2023.xlsx')

rows, cols = f.shape

print(f'Real Workload has {rows} rows and {cols} columns.')

print(f'Number of principal components: {n_components}.')
print(f'Number of clusters: {n_clusters}.')

# Dropping constant columns
print(*(f.columns[f.std() == 0]))
df = f.drop(columns=f.std()[f.std() == 0].index)

# Plotting the correlation matrix
plt.figure(figsize=(10, 5))
plt.matshow(df.corr(), cmap='gray', fignum=1)
plt.xticks(np.arange(df.shape[1]))
plt.yticks(np.arange(df.shape[1]))
plt.title('Correlation matrix')
plt.show()

# Create correlation matrix
corr_matrix = df.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find features with correlation greater than 0.99
to_drop = [column for column in upper.columns if any(upper[column] > 0.99)]

print(to_drop)

# Drop features 
df.drop(to_drop, axis=1, inplace=True)

# Z-score normalizatoin
df = df.apply(zscore)

# Principal Component Analysis
pca = PCA(n_components=n_components)
pca.fit(df)
df_transformed = pca.transform(df)

df_transformed = pd.DataFrame(df_transformed, columns=[f'PC_{i}' for i in range(1,n_components+1)])

components_variance = pca.explained_variance_ratio_

plt.figure(figsize=(15, 8))

plt.subplot(121)

plt.bar(x=np.arange(1, len(components_variance)+1), height=components_variance)
plt.title('Variance per Component')
plt.xticks(np.arange(1, len(components_variance)+1))
plt.xlabel('Component')
plt.ylabel('Variance')
plt.grid()

plt.subplot(122)

plt.plot(np.arange(1, len(components_variance)+1), components_variance.cumsum(), color='r', marker='o')
plt.title('Cumulative variance')
plt.xticks(np.arange(1, len(components_variance)+1))
plt.xlabel('Number of components')
plt.ylabel('Cumulative variance per Component')
plt.grid()

plt.show()

# Clustering
ward = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward', compute_distances=True)

ward.fit(df_transformed)    

clustering_history = pd.DataFrame({
                        'Numero di cluster': [i for i in range(1, rows)][::-1],
                        'Distanza': ward.distances_,
                        'Leader': [children[0] for children in ward.children_],
                        'Subordinato': [children[1] for children in ward.children_]
                    }).set_index('Numero di cluster')

plt.figure(figsize=(15, 8))
plt.plot(ward.distances_, [i for i in range(1, rows)][::-1], color='r', marker='o')
plt.title('Analisi di sensitività')
plt.xlabel('Distanza')
plt.ylabel('Numero di Cluster')
plt.ylim(top=50, bottom=0)
plt.grid(True)
plt.show()

print(clustering_history.tail(30))

plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(ward, labels=ward.labels_, orientation='right', truncate_mode='lastp', p=rows, no_labels=True)
plt.show()

df_transformed['Cluster'] = ward.labels_

# Histogram of clusters
cluster_labels = sorted(df_transformed['Cluster'].unique())
counts = df_transformed['Cluster'].value_counts()
bars = [counts[label] for label in cluster_labels]
plt.figure(figsize=(7,8))
plt.bar(cluster_labels, bars)
plt.title('Histogram of clusters')
plt.grid(True)
plt.show()

# Pre-PCA deviance
pre_pca_deviance = 0
centroid = df.mean(axis=0)
for row in df.iterrows():
    pre_pca_deviance += sum((row[1] - centroid)**2)
print(f'Pre-PCA deviance: {pre_pca_deviance}.')

# Post-PCA deviance
post_pca_deviance = 0
centroid = df_transformed.mean(axis=0)[:-1]
for row in df_transformed.iterrows():
    post_pca_deviance += sum((row[1][:-1] - centroid)**2)
print(f'Post-PCA deviance: {post_pca_deviance}.')

print(f'Variance preserved with {n_components} components: {post_pca_deviance/pre_pca_deviance:.2f}.')

# Intra-cluster deviance
clusters = sorted(df_transformed['Cluster'].unique())

intra_cluster_deviance = 0

for cluster in clusters:
    cluster_centroid = df_transformed.loc[df_transformed['Cluster'] == cluster].mean(axis=0)[:-1]
    for row in df_transformed.loc[df_transformed['Cluster'] == cluster].iterrows():
        intra_cluster_deviance += sum((row[1][:-1] - cluster_centroid)**2)

print(f'Intra-cluster deviance: {intra_cluster_deviance}.')

# Inter-cluster deviance
inter_cluster_deviance = 0

centroid = df_transformed.mean(axis=0)[:-1]

for cluster in clusters:
    cluster_centroid = df_transformed.loc[df_transformed['Cluster'] == cluster].mean(axis=0)[:-1]
    cluster_cardinality =  df_transformed.loc[df_transformed['Cluster'] == cluster].shape[0]
    inter_cluster_deviance += cluster_cardinality * sum((cluster_centroid - centroid)**2)

print(f'Inter-cluster deviance: {inter_cluster_deviance}.')

total_lost_deviance = (1 - post_pca_deviance/pre_pca_deviance) + intra_cluster_deviance/post_pca_deviance * post_pca_deviance/pre_pca_deviance
print(f'Total lost deviance: {total_lost_deviance}.')

synthetic_workload_indexes = []

for cluster in clusters:
    synthetic_workload_indexes.append(random.choice(df_transformed.index[df_transformed['Cluster'] == cluster].tolist()))

synthetic_workload = f.iloc[synthetic_workload_indexes]
synthetic_workload = synthetic_workload.drop(columns=synthetic_workload.std()[synthetic_workload.std() == 0].index)
synthetic_workload.to_excel('SyntheticWorkload.xlsx')
