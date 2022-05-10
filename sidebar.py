import streamlit as st
from seasons import seasons

def sidebar():
    st.sidebar.header('User Selections')

def select_season():
    return st.sidebar.selectbox('Choose a Season', seasons)

def select_team(teams):
    return st.sidebar.selectbox('Choose a team', teams)

def select_game(df):
    games = df[['Game Date', 'Game ID', 'Home Team', 'Away Team']]
    games['Game Date'] = games['Game Date'].astype('datetime64')
    games.sort_values('Game Date', ascending=True, inplace=True)
    games['Game Title'] = df['Game Date'] + ' ' + df['Away Team'] + ' at ' + df['Home Team'] 
    games.drop_duplicates(inplace=True)
    game_choice = st.sidebar.selectbox('Choose a game', games['Game Title'].unique())
    game = games[games['Game Title'] == game_choice]
    return game

def game_ind():
    return st.sidebar.checkbox('Would you like to view a specific game?')

def styler():
    choice = st.sidebar.selectbox('Choose Style of Shot Chart', ['Hex', 'KDE', 'Contour', 'Scatter'])
    return choice.lower()
