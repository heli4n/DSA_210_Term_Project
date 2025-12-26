import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/figures", exist_ok=True)

df = pd.read_csv("data/final_analysis.csv")

# Histogram
plt.figure()
plt.hist(df["female_ratio_totals"].dropna(), bins=30)
plt.xlabel("female_ratio_totals")
plt.ylabel("count")
plt.title("Distribution of female_ratio_totals")
plt.tight_layout()
plt.savefig("outputs/figures/fig1_ratio_hist.png", dpi=200)
plt.close()

# Boxplot
plt.figure()
plt.boxplot(df["female_ratio_totals"].dropna(), vert=False)
plt.xlabel("female_ratio_totals")
plt.title("Boxplot of female_ratio_totals")
plt.tight_layout()
plt.savefig("outputs/figures/fig1_ratio_box.png", dpi=200)
plt.close()

print("Saved:")
print(" - outputs/figures/fig1_ratio_hist.png")
print(" - outputs/figures/fig1_ratio_box.png")
