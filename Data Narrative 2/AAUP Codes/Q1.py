# Which state should an academician prefer to re-locate to based on the median of the average incomes of his/her rank across states (full, associate, assistant)?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from constants import *

for rank in ranks:
    A = avg_sal[rank]
    B = avg_comp[rank]
    C = 'State (Postal Code)'

    result = df.assign(income=df[A] + df[B]).groupby(C)['income'].median()
    result = result.sort_values(ascending=False) 
    plt.figure()
    pd.concat([result.head(5), result.tail(5)]).plot(kind='bar', color = "green")
    plt.title(f'Median Income of {ranks[rank]} Professors Statewise (Top 5, Bottom 5)', fontdict = font1)
    plt.xlabel('States', fontdict = font2)
    plt.ylabel('Median Salary (in dollars)', fontdict =  font2)
    labels = [us_states[item.get_text()] for item in plt.gca().get_xticklabels()]
    plt.gca().set_xticklabels(labels)
    plt.show()





