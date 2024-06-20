import pandas as pd
import matplotlib.pyplot as plt

books = pd.read_csv('../Goodreads_dataset/books.csv')

# Ploting number of ratings vs average rating
plt.scatter(books['average_rating'], books['ratings_count'])
plt.xlabel("Average rating")
plt.ylabel("Number of ratings")
plt.title("Plot of number of ratings vs average rating")
plt.grid()
plt.show()
