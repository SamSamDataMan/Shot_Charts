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
from court import draw_court, shot_chart_scatterplot, render_plot, shot_chart_hex, shot_chart_kde, shot_chart_contour

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

# fig = plot_shot_chart(shot_df, title, style)
if style == 'scatter':
    plot = shot_chart_scatterplot(shot_df)
elif style == 'hex':
    plot = shot_chart_hex(shot_df)
elif style == 'kde':
    plot = shot_chart_kde(shot_df)
elif style == 'contour':
    plot = shot_chart_contour(shot_df)


fig = render_plot(plot, title)
st.pyplot(fig)
