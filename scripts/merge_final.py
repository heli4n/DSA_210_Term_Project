import pandas as pd

df_img = pd.read_csv("data/df_country_ratios.csv")
df_vdem = pd.read_csv("data/merged_list.csv")

# If old female_ratio exists in V-Dem merged file, drop it to avoid confusion
if "female_ratio" in df_vdem.columns:
    df_vdem = df_vdem.drop(columns=["female_ratio"])

df = df_img.merge(df_vdem, on="country", how="inner")

required = ["v2x_polyarchy", "v2x_gender"]
missing = [c for c in required if c not in df.columns]
if missing:
    raise ValueError(f"Missing required columns after merge: {missing}")

df = df.dropna(subset=required).reset_index(drop=True)

df.to_csv("data/final_analysis.csv", index=False)

print("Saved: data/final_analysis.csv")
print("Rows:", len(df))
print("Columns:", list(df.columns))
print(df.head())
