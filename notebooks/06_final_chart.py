import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../processed_data/features_engineered.csv")

# Average depth per district
district_avg = df.groupby("District")["Depth_mbgl"].mean()

# Plot
plt.figure(figsize=(10,6))

district_avg.plot(
    kind="bar"
)

plt.title("Average Groundwater Depth by District")
plt.xlabel("District")
plt.ylabel("Depth Below Ground (m)")
plt.grid(axis="y")

# Save chart
plt.savefig("../outputs/final_district_chart.png")

# Show chart
plt.show()

print("Final chart created 🚀")