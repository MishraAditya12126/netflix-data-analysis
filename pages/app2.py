import streamlit as st
import show_analysis

st.set_page_config(
    page_title='Data Analysis',
    page_icon='📈',
    layout='wide'
)

st.header(':red[NETFLIX] Show Data Analysis')

year = st.sidebar.selectbox('Select a year',show_analysis.all_years())
btn = st.sidebar.button('Find Shows')

if btn:
    st.subheader(f'Top web series of year :blue[{year}]')
    df = show_analysis.best_shows_of_year(year)

    for i in range(df.shape[0]):
        x = df.iloc[i]
        if i%2 == 0:
                st.write(f"#:red[{i+1}]")
                st.write(f'Show title : :red[{x["title"]}]')
                st.write(f'Release year : :red[{x["release_year"]}]')
                st.write(f'No. of seasons : :red[{x["number_of_seasons"]}]')
                st.write(f'Genre : :red[{x["main_genre"]}]')

        else:
                st.write(f"#:green[{i+1}]")
                st.write(f'Show title : :green[{x["title"]}]')
                st.write(f'Release year : :green[{x["release_year"]}]')
                st.write(f'No. of seasons : :green[{x["number_of_seasons"]}]')
                st.write(f'Genre : :green[{x["main_genre"]}]')


genre = st.sidebar.selectbox('Choose a Genre',show_analysis.genres())
btn2 = st.sidebar.button('Find Genres')

if btn2:
    st.write(f'Top Shows in this genre :red[{genre}] are:')
    st.dataframe(show_analysis.top_shows((genre)))




