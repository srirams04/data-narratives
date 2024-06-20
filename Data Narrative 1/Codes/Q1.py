import pandas as pd
import matplotlib.pyplot as plt

# Loading the datasets
books = pd.read_csv('../Goodreads_dataset/books.csv')
user_to_read = pd.read_csv('../Goodreads_dataset/to_read.csv')

book_to_read = user_to_read.groupby(['book_id']).count()

# Merging the datasets on book ID
df = pd.merge(books.filter(['book_id', 'average_rating']), book_to_read, how = 'inner', on = 'book_id')

# Plotting number of interested readers vs average rating
plt.scatter(df['average_rating'], df['user_id'])
plt.xlabel("Average rating")
plt.ylabel("Number of interested readers (based on to-read)")
plt.title("Plot of number of interested readers vs average rating")
plt.grid()
plt.show()
