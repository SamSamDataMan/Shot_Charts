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
from sidebar import sidebar, select_season, select_team, select_game, game_ind, styler
from court import draw_court, plot_shot_chart

season = select_season()
base = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base, 'Data', 'NBA Shot Locations_' + season + '.csv'))

team_name = select_team(data['Team Name'].unique())

shot_df = data[(data['Team Name'] == team_name) & (data['Season'] == season)]
title = season + ' ' + team_name + ' Shot Chart'

if game_ind():
    game = select_game(shot_df)
    st.text(game)
    shot_df = shot_df[shot_df['Game ID'] == game['Game ID'].iloc[0]]
    game_name = game['Game Title'].iloc[0]
    title = game_name + ' ' + team_name + ' Shot Chart'

style = styler()

fig = plot_shot_chart(shot_df, title, style)
st.pyplot(fig)
