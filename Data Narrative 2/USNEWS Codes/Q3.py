# What is the trend in the average difference between the in-state tuition and the out-of-state tuition across the states?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

# load the csv file into a pandas dataframe
df = pd.read_csv('usnews.csv')

df['Out-of-state Tuition'] = df['Out-of-state Tuition'].mask(df['Out-of-state Tuition'] == '*', np.nan)
df['In-state Tuition'] = df['In-state Tuition'].mask(df['In-state Tuition'] == '*', np.nan)

df['Difference'] = df['Out-of-state Tuition'].astype(float) - df['In-state Tuition'].astype(float)
avg_diff = df.groupby('State (Postal Code)')['Difference'].mean()

# sort the states by average difference in tuition
state_diffs = avg_diff.sort_values()

# create a lollipop plot
fig, ax = plt.subplots()
ax.vlines(x=state_diffs.index, ymin=0, ymax=state_diffs.values, linewidth=2)
ax.plot(state_diffs.index, state_diffs.values, "o", markersize=8)

# format the plot
ax.set_xlabel('State (Postal Code)', fontdict = font2)
ax.set_ylabel('Average Difference in Tuition (Out-of-State - In-State)', fontdict = font2)
ax.set_title('Average Difference in Tuition by State', fontdict = font1)
plt.xticks(rotation=90)

plt.show()
