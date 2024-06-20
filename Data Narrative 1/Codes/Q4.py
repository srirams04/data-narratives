import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset
books = pd.read_csv('../Goodreads_dataset/books.csv')

# Computing the title length for each book
books['title_length'] = books['title'].str.len()

# Grouping books of the same publishing year together and finding the average title length
avg_title_length = books.groupby('original_publication_year')['title_length'].mean()

# Plotting average title length over the years
plt.bar(avg_title_length.index, avg_title_length.values)
plt.xlabel('Publication year')
plt.ylabel('Average title length')
plt.title('Average title length over the years')
plt.xlim(1850, 2000)

# Adding a trend line to the plot
z = np.polyfit(avg_title_length.index, avg_title_length.values, 50)
p = np.poly1d(z)
plt.plot(avg_title_length.index, p(avg_title_length.index), "r--")

plt.show()

