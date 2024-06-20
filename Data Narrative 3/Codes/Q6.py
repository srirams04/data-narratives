import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('./Tennis-Major-Tournaments-Match-Statistics/USOpen-women-2013.csv')

# Group the matches based on the round
grouped_df = df.groupby('ROUND')

# Calculate the average number of sets played in each round
average_sets = grouped_df['FNL.1'].mean() + grouped_df['FNL.2'].mean()
print(average_sets)

# Plot the lollipop graph
fig, ax = plt.subplots()
ax.stem(average_sets.index, average_sets, use_line_collection=True, basefmt=' ')

# Set the x-axis and y-axis labels
ax.set_xlabel('Round')
ax.set_ylabel('Average Sets Played')

# Set the title of the plot
ax.set_title('Average Number of Sets Played in Women\'s US Open 2013 Tournament by Round')

# Show the plot
plt.show()
