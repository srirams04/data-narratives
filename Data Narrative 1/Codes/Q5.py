import pandas as pd
import matplotlib.pyplot as plt

# Loading the dataset
books = pd.read_csv('../Goodreads_dataset/books.csv')

# Grouping books of the same publishing year together and finding the average title length
mod_rating_over_years = books.groupby('original_publication_year')['average_rating'].apply(lambda x: x.mode()[0])

# Plotting average title length over the years
plt.plot(mod_rating_over_years.index, mod_rating_over_years.values)
plt.xlabel('Publication year')
plt.ylabel('Most common book rating')
plt.title('Quality of books (based on mode ratings) over the years')
plt.xlim(1800, 2020)
plt.grid()
plt.show()

