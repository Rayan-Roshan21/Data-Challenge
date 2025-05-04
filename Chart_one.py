import pandas as pd
import matplotlib.pyplot as plt

# Load the immigration profile data
profile_df = pd.read_excel("ADA_profile_simplified.xlsx", engine="openpyxl")
# Load accessibility data
access_df = pd.read_excel("ADA_acs_file.xlsx", sheet_name="acs_ada_file")

# Define thresholds
public_ef_threshold = 0.5
walk_ef_threshold = 0.5

# Define "has access" (access via transit or walking)
access_df["has_access"] = (
    (access_df["public_ef"] > public_ef_threshold) | 
    (access_df["walk_ef"] > walk_ef_threshold)
)

# Merge on DAUID (update this key if needed)
merged_df = profile_df.merge(access_df, on="DAUID", how="inner")

# Filter immigrant and non-immigrant groups
immigrant_df = merged_df[merged_df["Characteristic"].str.contains("Immigrants", case=False, na=False)]
non_immigrant_df = merged_df[merged_df["Characteristic"].str.contains("Non-immigrants", case=False, na=False)]

# Calculate access rates
immigrant_access_pct = immigrant_df["has_access"].mean() * 100
non_immigrant_access_pct = non_immigrant_df["has_access"].mean() * 100

# Print results
print(f"Immigrant families with access: {immigrant_access_pct:.2f}%")
print(f"Non-immigrant families with access: {non_immigrant_access_pct:.2f}%")

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(["Immigrants"], [immigrant_access_pct], color='green', s=100, label="Immigrants")
plt.scatter(["Non-immigrants"], [non_immigrant_access_pct], color='blue', s=100, label="Non-immigrants")

plt.title("Scatter Plot of Childcare Access (%)")
plt.ylabel("Percentage with Access")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()
