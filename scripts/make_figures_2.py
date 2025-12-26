import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/figures", exist_ok=True)

df = pd.read_csv("data/final_analysis.csv").dropna(subset=["female_ratio_totals", "v2x_polyarchy", "n_images_people"])

x = df["v2x_polyarchy"].to_numpy()
y = df["female_ratio_totals"].to_numpy()
w = df["n_images_people"].to_numpy()

# scale sizes
sizes = 10 + 90 * (w - w.min()) / (w.max() - w.min() + 1e-9)

plt.figure()
plt.scatter(x, y, s=sizes, alpha=0.6)
plt.xlabel("v2x_polyarchy")
plt.ylabel("female_ratio_totals")
plt.title("Female representation vs Democracy (marker size = n_images_people)")
plt.tight_layout()
plt.savefig("outputs/figures/fig2_scatter_weighted.png", dpi=200)
plt.close()

print("Saved: outputs/figures/fig2_scatter_weighted.png")
