# Find the top 10 states to spend the highest amount on the salary and compensation of professors (all ranks)? This analysis is made to understand the educational inclination of different states.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from constants import *

A = avg_sal["all"]
B = avg_comp["all"]
C = num_of["all"]
D = "State (Postal Code)"

result = df.assign(income=(df[A] + df[B]) * df[C]).groupby(D)['income'].sum()
result = result.sort_values(ascending=False) 

plt.figure()
result = result / 1000000
result.head(10).plot(kind='bar')
plt.title(f'Total Expenditure on Professors (all ranks) Statewise', fontdict = font1)
plt.xlabel('States', fontdict = font2)
plt.ylabel('Total Expenditure (in million dollars)', fontdict =  font2)
labels = [us_states[item.get_text()] for item in plt.gca().get_xticklabels()]
plt.gca().set_xticklabels(labels)
plt.show()