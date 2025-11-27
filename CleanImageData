import os
import json
import pandas as pd

path = "/Users/ipekgezer/dataverse_files"

records = []

for folder in os.listdir(path): #getting the files
    full_path = os.path.join(path, folder) 

    if not os.path.isdir(full_path): #checking if it's a folder or not with os.path.isdir(which return true if it's a directory
        continue

    country = folder[:3] #folders' names' first three letters are shortened version of the countries' names 

    img_path = os.path.join(full_path, "images.jsonl")

    if not os.path.exists(img_path): #chechking if it exsists
        continue

    if os.path.getsize(img_path) == 0: #checking if it is empty or not
        continue

    with open(img_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                #getting the necessery informations
                obj = json.loads(line)
                male = obj.get("male-count", 0)
                female = obj.get("female-count", 0)
                total = male + female

                #creating a new list, and adding, if the total is bigger than zero (Because I don't want to have undefined results)
                if total > 0:
                     records.append({
                    "country": country,
                    "male_count": male,
                    "female_count": female,
                    "female_ratio": female / total 
                    })
            
            except:
                continue

df = pd.DataFrame(records)

df_avg = df.groupby("country")["female_ratio"].mean().reset_index() #getting the means by countries 

df_avg.to_csv("df_avg.csv", index=False) #downloding the data as csv file 
