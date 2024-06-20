# Universities on the east coast of the U.S. have strong competition with the ones on the west coast. They can be compared based on the proportion of full professors amongst the entire faculty considering only the top 5 colleges on each coast. The top 5 colleges are decided based on the amount spent on the faculty.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from constants import *

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

# Filter the colleges based on the states
west_coast_states = ['AK', 'AZ', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'NM', 'OR', 'UT', 'WA', 'WY']
df_west = df[df['State (Postal Code)'].isin(west_coast_states)]

# Calculate the amount spent on faculty
df_west['Amount Spent on Faculty'] = (df_west['Average Salary - All Ranks'] + df_west['Average Compensation - All Ranks']) * df_west['Number of Faculty - All Ranks']

# Sort the colleges based on the amount spent on faculty
df_west = df_west.sort_values(by=['Amount Spent on Faculty'], ascending=False)

# Take the top 5 colleges
df_west_top_5 = df_west.head(5)

# Calculate the proportion of full professors amongst total number of faculty
df_west_top_5['Proportion of Full Professors'] = df_west_top_5['Number of Full Professors'] / df_west_top_5['Number of Faculty - All Ranks']

# Filter the colleges based on the states
east_coast_states = ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY', 'NJ', 'PA', 'MD', 'DE', 'VA', 'NC', 'SC', 'GA', 'FL']
df_east = df[df['State (Postal Code)'].isin(east_coast_states)]

# Calculate the amount spent on faculty
df_east['Amount Spent on Faculty'] = (df_east['Average Salary - All Ranks'] + df_east['Average Compensation - All Ranks']) * df_east['Number of Faculty - All Ranks']

# Sort the colleges based on the amount spent on faculty
df_east = df_east.sort_values(by=['Amount Spent on Faculty'], ascending=False)

# Take the top 5 colleges
df_east_top_5 = df_east.head(5)

# Calculate the proportion of full professors amongst total number of faculty
df_east_top_5['Proportion of Full Professors'] = df_east_top_5['Number of Full Professors'] / df_east_top_5['Number of Faculty - All Ranks']

# Plot the bar graphs side by side
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

axs[0].bar(df_west_top_5['College Name'], df_west_top_5['Proportion of Full Professors'], color = "#3F7CE7")
axs[0].set_xticklabels(df_west_top_5['College Name'], rotation=60)
axs[0].set_xlabel('College Name', fontdict = font2)
axs[0].set_ylabel('Proportion of Full Professors', fontdict = font2)
axs[0].set_title('Top 5 Colleges by Amount Spent on Faculty - West Coast', fontdict = font1)

axs[1].bar(df_east_top_5['College Name'], df_east_top_5['Proportion of Full Professors'], color = "green")
axs[1].set_xticklabels(df_east_top_5['College Name'], rotation=60)
axs[1].set_xlabel('College Name', fontdict = font2)
axs[1].set_ylabel('Proportion of Full Professors', fontdict = font2)
axs[1].set_title('Top 5 Colleges by Amount Spent on Faculty - East Coast', fontdict = font1)

# Set the y-axis scale for both plots to be the same
axs[0].set_ylim([0, 1])
axs[1].set_ylim([0, 1])

plt.tight_layout()
plt.show()
