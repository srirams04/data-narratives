# What is the trend in the average of the total amount spent by students across the states? This analysis is made to help high school students from other countries decide a suitable state in the US to pursue further education based on their budget.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

# Read the csv file into a Pandas DataFrame
df = pd.read_csv('usnews.csv')


# Convert the numerical columns to integers
cols_to_convert = ['Out-of-state Tuition', 'Room and Board Costs', 'Additional Fees', 'Estimated Book Costs', 'Estimated Personal Spending']
for val in cols_to_convert:
    df[val] = df[val].mask(df[val] == '*', np.nan)

df[cols_to_convert] = df[cols_to_convert].astype(float)

# Calculate the sum of all costs and tuition fees for each state    
df['Total Cost'] = df[cols_to_convert].sum(axis=1)
avg_cost = df.groupby('State (Postal Code)')['Total Cost'].mean()

# sort the states by average difference in tuition
avg_cost = avg_cost.sort_values()

# Create a lollipop graph of the average total cost
fig, ax = plt.subplots()
ax.vlines(x=avg_cost.index, ymin=0, ymax=avg_cost.values, color='red', alpha=0.7, linewidth=2)
ax.scatter(x=avg_cost.index, y=avg_cost.values, s=75, color='red', alpha=0.7)

# Set the chart title and axis labels
ax.set_title('Average Total Cost by State', fontdict = font1)
ax.set_xlabel('State (Postal Code)', fontdict = font2)
ax.set_ylabel('Average Total Cost (in dollars)', fontdict = font2)

# Rotate the x-axis tick labels for better readability
plt.xticks(rotation=60, ha='right')

plt.show()