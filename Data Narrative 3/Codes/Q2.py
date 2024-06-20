import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from CSV file
data = pd.read_csv("./Tennis-Major-Tournaments-Match-Statistics/AusOpen-women-2013.csv")
finalist1 = []
finalist2 = []
x_labels = []
for i in range(1, 8):
    x1 = data[(data['Player1'] == "Na Li") & (data['Round'] == i)]
    x2 = data[(data['Player2'] == "Na Li") & (data['Round'] == i)]
    if not x1.empty:
        finalist1.append(x1["TPW.1"].to_list()[0]/(x1["TPW.2"].to_list()[0] + x1["TPW.1"].to_list()[0]))
    else:
        finalist1.append(x2["TPW.2"].to_list()[0]/(x2["TPW.1"].to_list()[0] + x2["TPW.2"].to_list()[0]))

    y1 = data[(data['Player1'] == "Dominika Cibulkova") & (data['Round'] == i)]
    y2 = data[(data['Player2'] == "Dominika Cibulkova") & (data['Round'] == i)]
    if not y1.empty: 
        finalist2.append(y1["TPW.1"].to_list()[0]/(y1["TPW.2"].to_list()[0] + y1["TPW.1"].to_list()[0]))
    else:
        finalist2.append(y2["TPW.2"].to_list()[0]/(y2["TPW.1"].to_list()[0] + y2["TPW.2"].to_list()[0]))

    x_labels.append(f"Round {i}")

print(finalist1)

# Set the width of each bar
bar_width = 0.25

# Create the x position of each bar
x_pos = np.arange(len(x_labels))

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(x_pos - bar_width, finalist1, bar_width, color='blue', label='Na Li')
ax.bar(x_pos, finalist2, bar_width, color='green', label='Dominika Cibulkova')

# Add labels, title and legend
ax.set_xlabel('Rounds')
ax.set_ylabel('Fraction of Total Points Scored')
ax.set_title('Fraction of total points scored by the finalists in each round')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.legend()

# Show the plot
plt.show()


"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from CSV file
data = pd.read_csv("./Tennis-Major-Tournaments-Match-Statistics/AusOpen-women-2013.csv")
finalist1 = []
finalist2 = []
x_labels = []
for i in range(1, 8):
    finalist1.extend(data[(data['Player1'] == "Na Li") & (data['Round'] == i)]["TPW.1"].to_list())
    finalist1.extend(data[(data['Player2'] == "Na Li") & (data['Round'] == i)]["TPW.2"].to_list())

    finalist2.extend(data[(data['Player1'] == "Dominika Cibulkova") & (data['Round'] == i)]["TPW.1"].to_list())
    finalist2.extend(data[(data['Player2'] == "Dominika Cibulkova") & (data['Round'] == i)]["TPW.2"].to_list())

    x_labels.append(f"Round{i}")

print(finalist1)

# Set the width of each bar
bar_width = 0.25

# Create the x position of each bar
x_pos = np.arange(len(x_labels))

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(x_pos - bar_width, finalist1, bar_width, color='blue', label='Na Li')
ax.bar(x_pos, finalist2, bar_width, color='green', label='Dominika Cibulkova')

# Add labels, title and legend
ax.set_xlabel('Rounds')
ax.set_ylabel('Total Points Scored')
ax.set_title('Total points scored by the finalists in each round')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.legend()

# Show the plot
plt.show()
"""