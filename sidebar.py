import streamlit as st
import pandas as pd
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
    games.drop_duplicates(inplace=True)
    games['Game Title'] = pd.to_datetime(games['Game Date']).dt.strftime('%d-%b-%Y') + ' - ' + df['Away Team'] + ' at ' + df['Home Team']
    game_choice = st.sidebar.selectbox('Choose a game', games['Game Title'].unique())
    game = games[games['Game Title'] == game_choice]
    return game

def select_player(df):
    players = df[['Player ID', 'Player Name']]
    players.sort_values('Player Name', ascending=True, inplace=True)
    players.drop_duplicates(inplace=True)
    player_choice = st.sidebar.selectbox('Choose a player', players['Player Name'].unique())
    player = players[players['Player Name'] == player_choice]
    return player

def game_ind():
    return st.sidebar.checkbox('Show me a specific game.')

def player_ind():
    return st.sidebar.checkbox('Show me a specific player.')

def styler():
    choice = st.sidebar.selectbox('Choose Style of Shot Chart', ['Scatter', 'Hex', 'KDE', 'Contour'])
    return choice.lower()

def levels():
    return st.sidebar.slider('Change Granularity', 5, 50, 30)
