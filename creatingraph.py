import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged = pd.read_csv("/content/merged_list.csv")

merged_cleaned = merged.dropna(subset=["female_ratio", "v2x_polyarchy"])
cleaned_rows = merged_cleaned.shape[0]

df_sorted = merged_cleaned.sort_values(by='v2x_polyarchy', ascending=True) #increasing order

plt.figure(figsize=(30, 18))

# bar plot for democracy index
sns.barplot(
    x='country',
    y='v2x_polyarchy',
    data=df_sorted,
    color='skyblue',
    label='(v2x_polyarchy)'
)

# line plot for female ratio
ax2 = plt.twinx()
sns.lineplot(
    x='country',
    y='female_ratio',
    data=df_sorted,
    ax=ax2,
    color='red',
    marker='o',
    linewidth=1.1,
    markersize=5,
    label='(female_ratio)'
)

# I've tried to rotate the country names to make them readable but couldn't manage it
ticks = range(len(df_sorted))
plt.xticks(rotation=90)

plt.ylabel('(v2x_polyarchy)', color='skyblue', fontsize=14)
plt.yticks(color='skyblue')

ax2.set_ylabel('(female_ratio)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

plt.legend(loc='upper left', fontsize=12)
ax2.legend(loc='upper right', fontsize=12)

plt.grid(axis='y', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()
