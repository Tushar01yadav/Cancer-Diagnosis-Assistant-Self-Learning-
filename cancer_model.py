import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score
import pickle

# Load breast cancer dataset
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

# Feature selection using RandomForest feature importances
rf = RandomForestClassifier(random_state=42)
rf.fit(X, y)
importances = rf.feature_importances_
feat_importances = pd.Series(importances, index=X.columns)
top6_features = feat_importances.nlargest(6).index.tolist()
print(top6_features)
# Select top 6 features
X_selected = X[top6_features]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=42)

# Train RandomForestClassifier on selected features
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Selected features:", top6_features)
data = [20.5,25.4,140.5,1325.0,0.125,0.3]
data_reshaped = np.array(data).reshape(1, -1)
prediction = clf.predict(data_reshaped)
print(prediction)
# Pickle the model
with open('rfe_model.pkl', 'wb') as f:
    pickle.dump( clf,f)
with open('selected_features.pkl', 'wb') as f:
    pickle.dump(top6_features, f)