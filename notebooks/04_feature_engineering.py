import pandas as pd

# Load dataset
df = pd.read_csv("../processed_data/master_dataset.csv")

# Sort values
df = df.sort_values(["District", "Year"])

# ------------------------------
# FEATURE 1: Water Depth Change
# ------------------------------
df["depth_change"] = (
    df.groupby("District")["Depth_mbgl"].diff()
)

# ------------------------------
# FEATURE 2: 3-Year Average
# ------------------------------
df["avg_depth_3yr"] = (
    df.groupby("District")["Depth_mbgl"]
    .transform(lambda x: x.rolling(3, min_periods=1).mean())
)

# ------------------------------
# FEATURE 3: Rainfall Deficit
# ------------------------------
NORMAL_RAINFALL = 600

df["rainfall_deficit"] = (
    NORMAL_RAINFALL - df["Annual_Rainfall_mm"]
)

# ------------------------------
# FEATURE 4: Stress Index
# ------------------------------
df["stress_index"] = (
    df["Depth_mbgl"] * 0.5 +
    df["rainfall_deficit"] * 0.02
)

# Replace missing values
df = df.fillna(0)

# Print output
print(df.head())

# Save file
df.to_csv(
    "../processed_data/features_engineered.csv",
    index=False
)

print("\nFeature engineering completed 🚀")