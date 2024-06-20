import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

books = pd.read_csv('../Goodreads_dataset/books.csv')
arr = np.array(list(x.count(',') + 1 for x in books['authors']))
unique, counts = np.unique(arr, return_counts=True)

df = pd.DataFrame({"Number of Authors": unique, "Number of Books": counts})
print(df)
