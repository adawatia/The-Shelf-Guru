import pandas as pd
import numpy as np

books = pd.read_csv("./Datasets/Books.csv")
users = pd.read_csv("./Datasets/Users.csv")
ratings = pd.read_csv("./Datasets/Ratings.csv")

books_with_rating = ratings.merge(books, on = "ISBN")
number_rating_dataframe = books_with_rating.groupby('Book-Title').count()['Book-Rating'].reset_index().rename(columns={'Book-Rating':'Number of Ratings'})
print(number_rating_dataframe)



print("Exit...")