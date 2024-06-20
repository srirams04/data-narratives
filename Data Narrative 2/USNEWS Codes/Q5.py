# Does alumni donation depend on whether the college is public or private? 
import pandas as pd
import numpy as np

# Load the csv file into a pandas dataframe
df = pd.read_csv('usnews.csv')

# Convert the numerical columns to integers
val = "Pct. Alumni who donate"
df[val] = df[val].mask(df[val] == '*', np.nan)

# Convert the data type of "Public/Private Indicator" column to integer
df['Public/Private Indicator'] = df['Public/Private Indicator'].astype(int)

# Replace 1 with "Public" and 2 with "Private" in "Public/Private Indicator" column
df['Public/Private Indicator'] = df['Public/Private Indicator'].replace({1: 'Public', 2: 'Private'})

# Convert the data type of "Pct. Alumni who donate" column to integer
df['Pct. Alumni who donate'] = df['Pct. Alumni who donate'].astype(float)

# Group the data by the "Public/Private Indicator" column and calculate the average of "Pct. Alumni who donate" for each group
result = df.groupby('Public/Private Indicator')['Pct. Alumni who donate'].mean()

# Print the result
print(result)

"""
Public/Private Indicator
Private    24.582873
Public     13.449438
"""