import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from CSV file
data = pd.read_csv("./Tennis-Major-Tournaments-Match-Statistics/FrenchOpen-men-2013.csv")
finalist1_ufe = []
finalist2_ufe = []
x_labels = []

for i in range(1, 8):
    finalist1_ufe.extend(data[(data['Player1'] == "Rafael Nadal") & (data['Round'] == i)]["UFE.1"].to_list())
    finalist1_ufe.extend(data[(data['Player2'] == "Rafael Nadal") & (data['Round'] == i)]["UFE.2"].to_list())

    finalist2_ufe.extend(data[(data['Player1'] == "David Ferrer") & (data['Round'] == i)]["UFE.1"].to_list())
    finalist2_ufe.extend(data[(data['Player2'] == "David Ferrer") & (data['Round'] == i)]["UFE.2"].to_list())

    x_labels.append(f"Round{i}")

print(finalist1_ufe)

# Set the width of each bar
bar_width = 0.25

# Create the x position of each bar
x_pos = np.arange(len(x_labels))

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(x_pos - bar_width, finalist1_ufe, bar_width, color='red', label='Rafael Nadal')
ax.bar(x_pos, finalist2_ufe, bar_width, color='black', label='David Ferrer')

# Add labels, title and legend
ax.set_xlabel('Rounds')
ax.set_ylabel('Unforced Errors Committed')
ax.set_title('Unforced errors committed by the finalists in each round')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.legend()

# Show the plot
plt.show()


finalist1_dbf = []
finalist2_dbf = []

for i in range(1, 8):
    finalist1_dbf.extend(data[(data['Player1'] == "Rafael Nadal") & (data['Round'] == i)]["DBF.1"].to_list())
    finalist1_dbf.extend(data[(data['Player2'] == "Rafael Nadal") & (data['Round'] == i)]["DBF.2"].to_list())

    finalist2_dbf.extend(data[(data['Player1'] == "David Ferrer") & (data['Round'] == i)]["DBF.1"].to_list())
    finalist2_dbf.extend(data[(data['Player2'] == "David Ferrer") & (data['Round'] == i)]["DBF.2"].to_list())


print(finalist1_dbf)

# Set the width of each bar
bar_width = 0.25

# Create the x position of each bar
x_pos = np.arange(len(x_labels))

# Create the bar plot
fig, ax = plt.subplots()
ax.bar(x_pos - bar_width, finalist1_dbf, bar_width, color='red', label='Rafael Nadal')
ax.bar(x_pos, finalist2_dbf, bar_width, color='black', label='David Ferrer')

# Add labels, title and legend
ax.set_xlabel('Rounds')
ax.set_ylabel('Double Faults Committed')
ax.set_title('Double faults committed by the finalists in each round')
ax.set_xticks(x_pos)
ax.set_xticklabels(x_labels)
ax.legend()

# Show the plot
plt.show()