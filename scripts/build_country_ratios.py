#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
import json
import pandas as pd

# input folder (your dataset root)
path = "/Users/ipekgezer/dataverse_files"

# output folder inside repo
os.makedirs("data", exist_ok=True)

rows = []

for folder in os.listdir(path):  # getting the files
    full_path = os.path.join(path, folder)

    if not os.path.isdir(full_path):  # checking if it's a folder or not
        continue

    country = folder[:3]  # folders' names' first three letters are shortened version of the countries' names
    img_path = os.path.join(full_path, "images.jsonl")

    if not os.path.exists(img_path):  # checking if it exists
        continue

    if os.path.getsize(img_path) == 0:  # checking if it is empty or not
        continue

    n_images_all = 0          # total images
    n_images_people = 0       # images with at least 1 person in it
    total_male = 0
    total_female = 0
    total_people = 0
    image_ratios = []         # female/total

    with open(img_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            n_images_all += 1

            # getting the necessary informations
            male = obj.get("male-count", 0) or 0
            female = obj.get("female-count", 0) or 0
            total = male + female

            if total == 0:
                continue

            n_images_people += 1
            total_male += male
            total_female += female
            total_people += total

            image_ratios.append(female / total)

    ratio_of_totals = (total_female / total_people) if total_people > 0 else None
    mean_image_ratio = (sum(image_ratios) / len(image_ratios)) if len(image_ratios) > 0 else None

    # creating a new list and adding it 
    rows.append({
        "country": country,
        "n_images_all": n_images_all,
        "n_images_people": n_images_people,
        "n_male": total_male,
        "n_female": total_female,
        "n_people": total_people,
        "female_ratio_totals": ratio_of_totals,   # main metric
        "female_ratio_meanimg": mean_image_ratio  # robustness metric
    })

df_country = pd.DataFrame(rows)

# keep only countries where we have at least 1 detected person overall
df_country = df_country[df_country["n_people"] > 0].reset_index(drop=True)

# save inside repo/data
out_path = "data/df_country_ratios.csv"
df_country.to_csv(out_path, index=False)

print(f"Saved: {out_path}")
print(df_country.head())

