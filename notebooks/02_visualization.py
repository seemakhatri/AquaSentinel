import pandas as pd
import matplotlib.pyplot as plt

# Load groundwater data
df = pd.read_csv("../raw_data/groundwater_rajasthan_clean.csv")

# Filter Ajmer only
ajmer = df[df["District"] == "Ajmer"]
jaisalmer = df[df["District"] == "Jaisalmer"]

# Create graph
plt.figure(figsize=(10,5))

plt.plot(
    ajmer["Year"],
    ajmer["Depth_mbgl"],
    marker="o",
    linewidth=3
)

# IMPORTANT:
# deeper water table = worse
plt.gca().invert_yaxis()

plt.title("Ajmer Groundwater Depth Trend")
plt.xlabel("Year")
plt.ylabel("Depth Below Ground Level (m)")
plt.grid(True)

# Save graph
plt.savefig("../outputs/ajmer_groundwater_trend.png")

# Show graph
plt.show()

print("Visualization created successfully 🚀")