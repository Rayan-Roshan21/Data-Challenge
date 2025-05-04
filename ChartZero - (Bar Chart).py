import pandas as pd
import matplotlib.pyplot as plt

# Here we're are loading the data
df = pd.read_excel("ADA_acs_file.xlsx", sheet_name="acs_ada_file")

# Here are threshold.
public_ef_threshold = 0.5
walk_ef_threshold = 0.5

# Flags for each mode
df['low_access_public'] = df['public_ef'] <= public_ef_threshold
df['low_access_walk'] = df['walk_ef'] <= walk_ef_threshold

# Filter for values that are focused in the GTA.
df_gta = df[df['CMAUID'] == 535]

# Counting True/False for each mode
public_counts = df_gta['low_access_public'].value_counts().sort_index()
walk_counts = df_gta['low_access_walk'].value_counts().sort_index()

# Create a new DataFrame to combine both counts.
counts_df = pd.DataFrame({
    'Public Transit': public_counts,
    'Walking': walk_counts
}).T 

# Plotting grouped bar chart
ax = counts_df.plot(kind='bar', figsize=(8, 6), color=['blue', 'red'])
plt.title('Number of GTA Areas with Low Access to Child Care by Mode')
plt.xlabel('Mode of Access')
plt.ylabel('Number of Areas')
plt.xticks(rotation=0)
plt.legend(['Adequate Access (False)', 'Low Access (True)'])

# Adding value labels to the bar.
for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.tight_layout()
plt.grid(axis='y')
plt.show()
