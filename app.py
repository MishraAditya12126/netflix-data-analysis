import streamlit as st
import analysis
import numpy as np
import pandas as pd
st.set_page_config(
    page_title='Data Analysis',
    page_icon='📈',
    layout='wide'
)
st.title(':red[NETFLIX] Movies Data Analysis')

select_year = st.sidebar.selectbox('Select a  year',analysis.release_year())

st.subheader(f'Movies released in year {select_year}')
btn = st.sidebar.button('Find movies')
if btn:
    st.dataframe(analysis.movies_in_year(select_year))
