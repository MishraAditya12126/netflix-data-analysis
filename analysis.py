import numpy as np
import pandas as pd
movies = pd.read_csv('best_movies_netflix.csv')

def release_year():
    return sorted(list(movies['release_year'].unique()),reverse=True)

def movies_in_year(year):
    return movies[movies['release_year'] == year]

def genres():
    return sorted(list(movies['main_genre'].unique()))

def best_movies_in_genre(genre):
    return movies[movies['main_genre'] == genre].sort_values(by = ['score'],ascending=[False]).head(1)

def production_place():
    return sorted(movies['main_production'].unique())

def no_of_movies(prod_plce):
    temp_df = movies[movies['main_production']==prod_plce]
    temp_df = temp_df.groupby('release_year')['title'].count()
    temp_df.rename('No_of_Movies/per_year',inplace=True)
    return temp_df
def genre_details(genre):
    temp_df = movies[movies['main_genre'] == genre]
    rly = temp_df.groupby('release_year')['title'].count()
    prd = temp_df.groupby('main_production')['title'].count()
    prd.rename('no. of movies',inplace=True)
    return (temp_df['duration'].mean(),temp_df['score'].mean(),rly,prd)

def comp_prd_place(prd1,prd2):
    temp_df1 = movies[movies['main_production']==prd1]
    temp_df2 = movies[movies['main_production']==prd2]
    gnr1 = temp_df1.groupby('main_genre')['title'].count()
    gnr2 = temp_df2.groupby('main_genre')['title'].count()
    l = [(temp_df1.shape[0],temp_df2.shape[0]) , (gnr1,gnr2)]
    return l


# print(no_of_movies('US'))
# print(type(no_of_movies('US')))

print(comp_prd_place('US','IN'))