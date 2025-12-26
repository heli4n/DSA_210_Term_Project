import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("outputs/figures", exist_ok=True)

df = pd.read_csv("data/final_analysis.csv").dropna(subset=["female_ratio_totals", "v2x_polyarchy"])

df["poly_q"] = pd.qcut(df["v2x_polyarchy"], 4, labels=["Q1(low)", "Q2", "Q3", "Q4(high)"])

groups = [df.loc[df["poly_q"] == q, "female_ratio_totals"].dropna().to_list()
          for q in ["Q1(low)", "Q2", "Q3", "Q4(high)"]]

plt.figure()
plt.boxplot(groups, labels=["Q1(low)", "Q2", "Q3", "Q4(high)"])
plt.ylabel("female_ratio_totals")
plt.title("Female ratio by Democracy Quartiles (v2x_polyarchy)")
plt.tight_layout()
plt.savefig("outputs/figures/fig3_quartile_boxplot.png", dpi=200)
plt.close()

print("Saved: outputs/figures/fig3_quartile_boxplot.png")
