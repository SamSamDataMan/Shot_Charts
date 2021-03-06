# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:39:35 2021

@author: king2
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
import streamlit as st
from sidebar import sidebar, select_season, select_team, select_game, select_player, game_ind, player_ind, styler, levels
from court import draw_court, shot_chart_scatterplot, shot_chart_hex, shot_chart_kde, shot_chart_contour

@st.cache
def season_data(base, season):
    return pd.read_csv(os.path.join(base, 'Data', 'NBA Shot Locations_' + season + '.csv'))

season = select_season()
base = os.path.dirname(__file__)
data = season_data(base, season)

team_name = select_team(data['Team Name'].unique())

shot_df = data[(data['Team Name'] == team_name)]

title = season + ' ' + team_name + ' Shot Chart'
marker_size = 75  # parameter for scatterplot
grid_size = (20, 15)  # parameter for hexbin

if game_ind():
    marker_size = 150  # parameter for scatterplot
    grid_size = (7, 3)  # parameter for hexbin
    game = select_game(shot_df)
    shot_df = shot_df[shot_df['Game ID'] == game['Game ID'].iloc[0]]
    game_name = game['Game Title'].iloc[0]
    title = game_name + ' --- ' + team_name + ' Shot Chart'

if player_ind():
    marker_size = 300
    player = select_player(shot_df)
    shot_df = shot_df[shot_df['Player ID'] == player['Player ID'].iloc[0]]
    title = player['Player Name'].iloc[0] + ' --- ' + title

if len(list(shot_df['Shot Made Flag'].unique())) == 2:
    markers = ['X', 'o']
    palette = ['r', 'g']
else:
    if list(shot_df['Shot Made Flag'].unique())[0] == 0:
        markers = ['X']
        palette = ['r']
    else:
        markers = ['o']
        palette = ['g']

style = styler()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

draw_court(fig, ax)

if style == 'scatter':
    plot = shot_chart_scatterplot(shot_df, marker_size, markers, palette)
elif style == 'hex':
    plot = shot_chart_hex(shot_df, grid_size)
elif style == 'kde':
    level = levels()
    plot = shot_chart_kde(shot_df, level)
elif style == 'contour':
    level = levels()
    plot = shot_chart_contour(shot_df, level)

plt.title(title)
st.pyplot(fig)
