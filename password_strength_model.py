import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import math

# Example password dataset
data = pd.DataFrame({
    'length': [6, 8, 12, 10, 7, 15],
    'has_upper': [0, 1, 1, 1, 0, 1],
    'has_digit': [0, 1, 1, 1, 0, 1],
    'has_special': [0, 1, 1, 0, 0, 1],
    'entropy': [2.0, 4.5, 8.0, 6.0, 3.0, 10.0],
    'label': [0, 1, 2, 1, 0, 2]  # 0: Weak, 1: Moderate, 2: Strong
})

# Features and target
X = data[['length', 'has_upper', 'has_digit', 'has_special', 'entropy']]
y = data['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'password_strength_model.pkl')
print("Model trained and saved as password_strength_model.pkl")
