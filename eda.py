import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
feature_names = [ 'radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']

df.head()
df = pd.DataFrame(data.data, columns=feature_names)
df['target'] = data.target
correlation_with_target = df.corr()['target'].drop('target')
threshold = 0.4
important_features = correlation_with_target[correlation_with_target.abs() >= threshold].index.tolist()
df_important = df[important_features]
corr_matrix = df_important.corr().abs()
# Upper triangle matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
reduced_features = [f for f in important_features if f not in to_drop]

new_df_var = reduced_features +['target']
df = df[new_df_var]
df.shape




