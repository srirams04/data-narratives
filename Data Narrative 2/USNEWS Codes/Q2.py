# Consider Harvard University, Massachusetts Institute of Technology (MIT), Stanford University, California Institute of Technology (Caltech) and Yale University, which are among the top 10 colleges in the US. Compare the acceptance and joining rates of these colleges.

import pandas as pd
import matplotlib.pyplot as plt

font1 = {'family':'Sans','color':'blue','size':18}
font2 = {'family':'serif','color':'darkred','size':15}

# load data from csv file
df = pd.read_csv("usnews.csv")

# filter data to include only relevant colleges
relevant_colleges = ["Harvard University", "Massachusetts Institute of Technology", 
                     "Stanford University", "California Institute of Technology", 
                     "Yale University"]
df = df[df["College Name"].isin(relevant_colleges)]

# convert data to integer format
df["Number of Applications Received"] = df["Number of Applications Received"].astype(int)
df["Number of Applicants Accepted"] = df["Number of Applicants Accepted"].astype(int)
df["Number of New Students Enrolled"] = df["Number of New Students Enrolled"].astype(int)

# calculate acceptance and enrollment rates
df["Acceptance Rate"] = df["Number of Applicants Accepted"] / df["Number of Applications Received"] * 100
df["Enrollment Rate"] = df["Number of New Students Enrolled"] / df["Number of Applications Received"] * 100

# create line plot
fig, ax1 = plt.subplots()

# set axis labels and title
ax1.set_xlabel("College", fontdict = font2)
ax1.set_ylabel("Acceptance Rate (%)", color="tab:blue", fontdict = font2)
ax1.set_title("Acceptance and Enrollment Rates at Top US Universities", fontdict = font1)
ax1.tick_params(axis='y', labelcolor="tab:blue")

# plot acceptance rates
ax1.plot(df["College Name"], df["Acceptance Rate"], color="tab:blue", marker="o")

# create second y-axis
ax2 = ax1.twinx()

# set axis label and color
ax2.set_ylabel("Enrollment Rate (%)", color="tab:green", fontdict = font2)
ax2.tick_params(axis='y', labelcolor="tab:green")

# plot enrollment rates
ax2.plot(df["College Name"], df["Enrollment Rate"], color="tab:green", marker="o")

# display plot
plt.show()
