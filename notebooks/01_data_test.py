import pandas as pd

groundwater = pd.read_csv("../raw_data/groundwater_rajasthan.csv")
rainfall = pd.read_csv("../raw_data/rainfall_rajasthan.csv")

print("Groundwater Data:")
print(groundwater.head())

print("\nRainfall Data:")
print(rainfall.head())