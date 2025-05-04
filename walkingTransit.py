import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the given excel files.
df = pd.read_excel("ADA_acs_file.xlsx", sheet_name="acs_ada_file")

# These are thresholds that we used to decide if someone 
# has good access to the child care via walking or using transit
public_ef_threshold = 0.4
walk_ef_threshold = 0.4

# Here we filtering out the data based on the threshold.
df['low_access'] = (
    (df['public_ef'] <= public_ef_threshold) &
    (df['walk_ef'] <= walk_ef_threshold)
)

# Here we're visualizing the data based on a true and false system. 
# Specifically, if true then it means that a row's values are below or equal to both thresholds and thus, low access to child care services.
# If false, meaning better access to at least one of the services.
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='public_ef',
    y='walk_ef',
    hue='low_access',
    palette={True: 'red', False: 'blue'},
    alpha=0.6
)

# Here we're setting the chart's characteristics.
plt.title("Access to Child Care Services (Thresholds -> 0.4)")
plt.xlabel("Access via Public Transit")
plt.ylabel("Access via Walking")
plt.legend(title="Low Access (< 0.4)")
plt.grid(True)
plt.show()


# Count number of low and non-low access neighborhoods
low_access_counts = df['low_access'].value_counts()
print(low_access_counts)