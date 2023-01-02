import numpy as np
import pandas as pd

shows = pd.read_csv('best_shows_netflix.csv')

def all_years():
    return sorted(list(shows['release_year'].unique()),reverse=True)

def best_shows_of_year(year):
    return shows[shows['release_year'] == year].sort_values(by=['score','number_of_votes'],ascending=[False,False]).head()

def genres():
    return sorted(list(shows['main_genre'].unique()))

def top_shows(genre):
    return shows[shows['main_genre'] == genre].sort_values(by=['score'],ascending=False).head()

print(best_shows_of_year(2020).iloc[0])