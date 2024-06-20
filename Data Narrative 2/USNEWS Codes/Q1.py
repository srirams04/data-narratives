# Does the quality of students entering a college directly affect the graduation rate? Quality of students entering a college can be estimated based on the SAT scores. 10 colleges are to be selected randomly for the above study.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

# Load the data into a pandas dataframe
data = pd.read_csv("usnews.csv")

# Select 10 random colleges from the data
random_colleges = data.sample(n=10)

# Get the college names and scores for the x and y axes
x = random_colleges["College Name"]
y1 = random_colleges["Average Combined SAT score"]
y2 = random_colleges["Graduation rate"]

# Create a figure and two subplots with the same x-axis
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot the first lollipop plot on the first subplot
ax1.vlines(x, ymin=0, ymax=y1, color='blue', alpha=0.7, linewidth=1)
ax1.plot(x, y1, "o", markersize=5, color='blue', alpha=0.7)
ax1.set_xlabel('College Name', fontsize=12)
ax1.set_ylabel('Average Combined SAT Score', color='b', fontsize=12)
ax1.tick_params('y', colors='b')

# Plot the second lollipop plot on the second subplot
ax2.vlines(x, ymin=0, ymax=y2, color='red', alpha=0.7, linewidth=1)
ax2.plot(x, y2, "o", markersize=5, color='red', alpha=0.7)
ax2.set_ylabel('Graduation Rate', color='r', fontsize=12)
ax2.tick_params('y', colors='r')

ax1.invert_yaxis()
ax2.invert_yaxis()

# Set the layout to prevent the x-labels from overlapping
fig.autofmt_xdate(rotation=45)

plt.title("Comparison between SAT Scores and Graduation Rates of Random 10 Colleges", fontdict = font1)
# Show the plot
plt.show()
