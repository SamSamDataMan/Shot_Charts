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
from sidebar import sidebar, season_select, styler
from court import draw_court
from court import plot_shot_density


team_id = 1610612744
# season = '2013-14'

season = season_select()


base = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base, 'Data', 'NBA Shot Locations_' + season + '.csv'))

shot_df = data[(data['Team ID'] == team_id) & (data['Season'] == season)]


team_name = shot_df['Team Name'].unique()[0]
st.text(team_name)

style = styler()

fig = plot_shot_density(shot_df, team_name, season, style)
st.pyplot(fig)
