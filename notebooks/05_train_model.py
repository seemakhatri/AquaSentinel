import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../processed_data/features_engineered.csv")

# Features
X = df[[
    "Depth_mbgl",
    "Annual_Rainfall_mm",
    "depth_change",
    "avg_depth_3yr",
    "rainfall_deficit",
    "stress_index"
]]

# Target
y = df["risk_label"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
model = RandomForestClassifier(
    n_estimators=100,
     max_depth=4,  
         min_samples_split=5, 
    min_samples_leaf=3,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nPredictions:")
print(predictions)

print("\nAquaSentinel ML Model Completed 🚀")