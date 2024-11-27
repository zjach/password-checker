import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Create a synthetic dataset with corrected parameters
X, y = make_classification(n_samples=1000, n_features=5, n_classes=2, n_clusters_per_class=2, n_informative=2)

# Proceed with the rest of the code as usual

# Train a model (using RandomForestClassifier here for illustration)
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# Save the model
joblib.dump(model, 'password_strength_model.pkl')
