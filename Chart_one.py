import pandas as pd
import matplotlib.pyplot as plt

# Loading the datasets
acs_df = pd.read_excel("ADA_acs_file.xlsx", sheet_name=0)
profile_df = pd.read_csv("ADA_profile_simplified(csv).csv")

# Merge on CMAUID. This would help us get the values that have 535 area code.
merged = pd.merge(acs_df, profile_df, on="CMAUID", how="inner")

# Filter to GTA (CMAUID = 535)
gta = merged[merged["CMAUID"] == 535]

# Get population counts. We are splitting it up between immigrants and non_immigrants.
immigrants = gta["T1529"].sum()
non_immigrants = gta["T1528"].sum()

# Here we're creating the pie chart.
labels = ['Immigrants', 'Canadian-born']
sizes = [immigrants, non_immigrants]
colors = ['#007acc', '#f5a623']

# Here we are creating the plotting the pie chart and creating any necessary labels.
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Chart 1: % of Immigrant vs. Canadian-born Families in the GTA (CMA 535)')
plt.axis('equal')  # Equal aspect ratio ensures pie is circular
plt.tight_layout()
plt.show()
