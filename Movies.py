import streamlit as st
import analysis
import numpy as np
import pandas as pd
st.set_page_config(
    page_title='Data Analysis',
    page_icon='📈',
    layout='wide'
)
list_opt = ['Movies released in a year','Find Best movie in a genre','Movies production place','Comparison Between production place']
st.title(':red[NETFLIX] Movies Data Analysis')
option = st.sidebar.radio('Select any one option: ',list_opt)
tab1,tab2=st.tabs(["🗃 Data","📈 Chart"])

if option == list_opt[0]:
    select_year = st.sidebar.selectbox('Select a year',analysis.release_year())
    btn = st.sidebar.button('Release Analysis')
    if btn:
        df = analysis.movies_in_year(select_year)
        with tab1:
            st.subheader('Best movies to watch in :blue[2022]')
            for i in range(df.shape[0]):
                x = df.iloc[i]
                if i % 2 == 0:
                    st.markdown(f"# :red[{i + 1}]")
                    st.write(f'Show title : :red[{x["title"]}]')
                    st.write(f'Release year : :red[{x["release_year"]}]')
                    st.write(f'Genre : :red[{x["main_genre"]}]')

                else:
                    st.markdown(f"# :green[{i + 1}]")
                    st.write(f'Show title : :green[{x["title"]}]')
                    st.write(f'Release year : :green[{x["release_year"]}]')
                    st.write(f'Genre : :green[{x["main_genre"]}]')
            st.dataframe(df)
        with tab2:
            st.subheader(f'Some visuals for year :blue[{select_year}]')
            col1,col2 = st.columns(2)
            with col1:
                st.write(':red[Movies v]/s Genre')
                st.bar_chart(df.groupby('main_genre')['title'].count())
            with col2:
                st.write(':red[Movies v]/:green[s Production]')
                st.bar_chart(df.groupby('main_production')['title'].count())



if option == list_opt[1]:
    genre = st.sidebar.selectbox('Select a genre',analysis.genres())
    btn2 = st.sidebar.button('Genre Analysis')

    if btn2:
        df = analysis.best_movies_in_genre(genre)
        with tab1:
            st.subheader(f'Best {genre} movie is :green[{df["title"].values[0]}] ')
            st.write(df)
        with tab2:
            x = analysis.genre_details(genre)
            col1,col2 = st.columns(2)
            with col1:
                st.metric(f'Average duration of {genre}',str((round(x[0],2)))+' min')
                st.metric(f'Average score of {genre}',round(x[1],2))
            with col2:
                st.caption(f'Movies produced in :red[{genre}] genre by every country')
                st.bar_chart(x[3])
            st.write(f'No. of movies released every year in {genre}')
            st.line_chart(x[2])




if option == list_opt[2]:
    prod_plce = st.sidebar.selectbox('select a production Place',analysis.production_place())
    df = analysis.no_of_movies(prod_plce)
    st.subheader(f'# Number of movies produced every year in :blue[{prod_plce}]')
    btn3 = st.sidebar.button('Production Place Analysis')
    if btn3:
        st.bar_chart(df)


if option == list_opt[3]:
    prd_places = analysis.production_place()
    prd1 = st.sidebar.selectbox('Select a place1',prd_places)
    prd2 = st.sidebar.selectbox('select a place2',prd_places)

    btn4 = st.sidebar.button('Find Results')
    if btn4:
        st.subheader(f'Comparison Between {prd1} and {prd2} Production Place')
        l = analysis.comp_prd_place(prd1, prd2)
        col1, col2 = st.columns(2)
        with col1:
            st.metric(f'No. of movies made in {prd1}',l[0][0])
            st.bar_chart(l[1][0])
            st.info(f'{prd1} makes mostly {l[1][0].sort_values(ascending=False).head(1).index[0]}')
        with col2:
            st.metric(f'No. of movies made in {prd2}',l[0][1])
            st.bar_chart(l[1][1])
            st.info(f'{prd2} makes mostly {l[1][1].sort_values(ascending=False).head(1).index[0]}')


