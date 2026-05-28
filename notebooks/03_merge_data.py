import pandas as pd

# Load datasets
groundwater = pd.read_csv("../raw_data/groundwater_rajasthan_clean.csv")
rainfall = pd.read_csv("../raw_data/rainfall_rajasthan.csv")
labels = pd.read_csv("../raw_data/cgwb_labels.csv")

# Merge groundwater + rainfall
merged = pd.merge(
    groundwater,
    rainfall,
    on=["District", "Year"]
)


# Merge labels
merged = pd.merge(
    merged,
    labels,
    on="District"
)

# Show merged data
print("\nMerged Dataset:")
print(merged.head())

# Save final dataset
merged.to_csv("../processed_data/master_dataset.csv", index=False)

print("\nMaster dataset created successfully 🚀")