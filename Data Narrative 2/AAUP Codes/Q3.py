# As a follow-up to the purpose of Q2, find the total number of professors (all ranks) state by state.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from constants import *

A = num_of['all']
B = "State (Postal Code)"

result = df.groupby(B)[A].sum()
result = result.sort_values(ascending=False) 

plt.figure()
result.head(10).plot(kind='bar')
plt.title(f'Total Number on Faculty (all ranks) Statewise', fontdict = font1)
plt.xlabel('States', fontdict = font2)
plt.ylabel('Count of Faculty', fontdict =  font2)
labels = [us_states[item.get_text()] for item in plt.gca().get_xticklabels()]
plt.gca().set_xticklabels(labels)
plt.show()
