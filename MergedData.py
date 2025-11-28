import pandas as pd

df = pd.read_csv("/content/df_avg.csv")
vdem = pd.read_csv("/content/V-Dem-CY-Full+Others-v15.csv", low_memory=False)

countries = df["country"].unique()

vdem_after2000 = vdem[vdem["year"] >= 2000]
vdem_cleaned = vdem_after2000[["country_text_id", "v2x_polyarchy","v2x_gender"]]
vdem_filtered = vdem_cleaned[vdem_cleaned["country_text_id"].isin(countries)]

vdem_filtered_mean = vdem_filtered.groupby("country_text_id").mean()
merged_list = df.merge(vdem_filtered_mean, left_on="country", right_on="country_text_id", how="left")
merged_list = merged_list.drop(columns=["country_text_id"])

merged_list.to_csv("merged_list.csv", index=False)
