import streamlit as st
from seasons import seasons

def sidebar(shot_df, t1_shot_df, t1_players, t2_shot_df, t2_players):
    st.sidebar.header('User Selections')

def season_select():
    return st.sidebar.selectbox('Choose a Season', seasons)
    
def styler():
    choice = st.sidebar.selectbox('Choose Style of Shot Chart', ['Hex', 'KDE', 'Contour', 'Scatter'])
    return choice.lower()

