import pandas as pd

# Load real dataset
df = pd.read_csv(
    "../raw_data/Atal_Jal_Disclosed_Ground_Water_Level-2015-2022.csv",
    encoding="latin1"
)

# Keep only needed columns
cleaned = pd.DataFrame()

# Extract district name
cleaned["District"] = (
    df["District_Name_With_LGD_Code"]
    .str.split("_")
    .str[0]
)

# Use 2022 pre-monsoon groundwater depth
cleaned["Depth_mbgl"] = pd.to_numeric(
    df["Pre-monsoon_2022 (meters below ground level)"],
    errors="coerce"
)

# Add year
cleaned["Year"] = 2022

# Add season
cleaned["Season"] = "Pre-Monsoon"

# Remove missing values
cleaned = cleaned.dropna()

# Keep only realistic groundwater values
cleaned = cleaned[
    (cleaned["Depth_mbgl"] > 0) &
    (cleaned["Depth_mbgl"] < 100)
]

# Rajasthan districts only (important)
rajasthan_districts = [
    "Ajmer", "Jaipur", "Jodhpur", "Jaisalmer",
    "Barmer", "Bikaner", "Nagaur", "Udaipur",
    "Kota", "Churu"
]

cleaned = cleaned[
    cleaned["District"].isin(rajasthan_districts)
]

# Save cleaned dataset
cleaned.to_csv(
    "../raw_data/groundwater_rajasthan_real.csv",
    index=False
)

print(cleaned.head())

print("\nRows:", len(cleaned))

print("\nReal groundwater dataset cleaned successfully 🚀")