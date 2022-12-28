import numpy as np
import pandas as pd
movies = pd.read_csv('best_movies_netflix.csv')

def release_year():
    return sorted(list(movies['release_year'].unique()),reverse=True)

def movies_in_year(year):
    return movies[movies['release_year'] == year]