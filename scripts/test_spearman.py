import os
import pandas as pd
from scipy.stats import spearmanr

os.makedirs("outputs/tables", exist_ok=True)

df = pd.read_csv("data/final_analysis.csv")

def run(a, b):
    sub = df[[a, b]].dropna()
    rho, p = spearmanr(sub[a], sub[b])
    return {"x": a, "y": b, "n": len(sub), "spearman_rho": rho, "p_value": p}

results = [
    run("v2x_polyarchy", "female_ratio_totals"),
    run("v2x_gender", "female_ratio_totals"),
    run("v2x_polyarchy", "female_ratio_meanimg"),
    run("v2x_gender", "female_ratio_meanimg"),
]

out = pd.DataFrame(results)
out.to_csv("outputs/tables/table1_spearman.csv", index=False)

print("Saved: outputs/tables/table1_spearman.csv")
print(out)
