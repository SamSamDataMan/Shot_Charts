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
from sidebar import sidebar, select_season, select_team, styler
from court import draw_court
from court import plot_shot_density

season = select_season()
base = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base, 'Data', 'NBA Shot Locations_' + season + '.csv'))

team_name = select_team(data['Team Name'].unique())

shot_df = data[(data['Team Name'] == team_name) & (data['Season'] == season)]

style = styler()

fig = plot_shot_density(shot_df, team_name, season, style)
st.pyplot(fig)
