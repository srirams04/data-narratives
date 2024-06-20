import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from CSV file
data = pd.read_csv("./Tennis-Major-Tournaments-Match-Statistics/Wimbledon-men-2013.csv")

# Create a scatter plot of aces vs result
plt.scatter(data["ACE.1"], data["WNR.1"])
plt.scatter(data["ACE.2"], data["WNR.2"])

# Set the labels for the plot
plt.title("Correlation between the number of aces served and winners hit")
plt.xlabel("Number of Aces")
plt.ylabel("Number of Winners")

# Show the plot
plt.show()
