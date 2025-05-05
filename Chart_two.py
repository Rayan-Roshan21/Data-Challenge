import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Here's the data based on the 2021 Census for the Toronto CMA (GTA)
data = {
    'Municipality': [
        'Markham (City)', 'Richmond Hill (Town)', 'Mississauga (City)',
        'Brampton (City)', 'Toronto (City)', 'Vaughan (City)',
        'Milton (Town)', 'Ajax (Town)', 'Oakville (Town)', 'Aurora (Town)',
        'Pickering (City)', 'Whitchurch-Stouffville (Town)', 'Newmarket (Town)',
        'Bradford West Gwillimbury (Town)', 'Caledon (Town)', 'East Gwillimbury (Town)',
        'King (Township)', 'Halton Hills (Town)', 'Georgina (Town)',
        'Orangeville (Town)', 'Uxbridge (Township)'
    ],
    'Total Population': [
        337250, 200925, 712825, 650165, 2761285, 321315, 131430, 126245,
        212055, 61390, 98580, 49420, 86615, 42335, 76085, 34125, 27205,
        62330, 47130, 29690, 21405
    ],
    'Immigrant Population (Number)': [
        197540, 116855, 379420, 343690, 1286145, 149240, 55270, 52745,
        87345, 22570, 35780, 17450, 28950, 13825, 22220, 9845, 7070,
        11840, 7515, 4335, 2890
    ],
    'Immigrant Population (%)': [
        58.6, 58.2, 53.2, 52.9, 46.6, 46.4, 42.1, 41.8, 41.2, 36.8, 36.3,
        35.3, 33.4, 32.7, 29.2, 28.8, 26.0, 19.0, 15.9, 14.6, 13.5
    ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# --- Plot 1: Immigrant Population Percentage ---

# Sort by percentage for better visualization
df_sorted_pct = df.sort_values('Immigrant Population (%)', ascending=False)

plt.figure(figsize=(14, 7)) # Increase figure size for readability
bars_pct = plt.bar(df_sorted_pct['Municipality'], df_sorted_pct['Immigrant Population (%)'], color='skyblue')

# Add percentage labels on top of bars
for bar in bars_pct:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.1f}%', va='bottom', ha='center') # Adjust position slightly

# Here is the data visualization tools for graph 1.
plt.xlabel("Municipality")
plt.ylabel("Immigrant Population (%)")
plt.title("Percentage of Population who are Immigrants in GTA Municipalities (2021 Census)")
plt.xticks(rotation=75, ha='right') # Rotate labels and align them
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter()) # Format y-axis as percentage
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to prevent labels overlapping
plt.show()

# Graph 2: Absolute Immigrant Population Number ---

# Sort by absolute number for better visualization
df_sorted_num = df.sort_values('Immigrant Population (Number)', ascending=False)

plt.figure(figsize=(14, 7)) # Increase figure size
bars_num = plt.bar(df_sorted_num['Municipality'], df_sorted_num['Immigrant Population (Number)'], color='lightcoral')

# Here is the data visualization tools for graph 2.
plt.xlabel("Municipality")
plt.ylabel("Number of Immigrants")
plt.title("Absolute Number of Immigrants in GTA Municipalities (2021 Census)")
plt.xticks(rotation=75, ha='right') # Rotate labels and align them
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, p: format(int(x), ','))) # Format y-axis with commas
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout
plt.show()
