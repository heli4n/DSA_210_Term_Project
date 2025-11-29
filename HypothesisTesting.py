import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

merged = pd.read_csv("/content/merged_list.csv")

merged_cleaned = merged.dropna(subset=["female_ratio", "v2x_polyarchy"]) #drop empty cells
cleaned_rows = merged_cleaned.shape[0]

# Spearman test
rho, pval = spearmanr(merged_cleaned["female_ratio"], merged_cleaned["v2x_polyarchy"]) #spearman correlation coefiecent and p-value
print("Spearman rho:", rho)
print("p-value:", pval)


#visualising
plt.figure(figsize=(16,12))
plt.scatter(merged_cleaned["female_ratio"], merged_cleaned["v2x_polyarchy"])

for i, row in merged_cleaned.iterrows():
    plt.text(row["female_ratio"], row["v2x_polyarchy"], row["country"], fontsize=8)

plt.xlabel("Female Ratio in News Images")
plt.ylabel("Democracy Score (v2x_polyarchy)")
plt.title("Female Representation vs Democracy Level")
plt.grid(True)
plt.show()
