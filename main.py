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
from sidebar import sidebar, styler
from court import draw_court
from court import plot_shot_density

base = os.path.dirname(__file__)
data = pd.read_csv(os.path.join(base, 'Data', 'NBA Shot Locations_Clean.csv'))

team_id = 1610612764
season = '2013-14'

shot_df = data[(data['Team ID'] == team_id) & (data['Season'] == season)]

style = styler()

fig = plot_shot_density(shot_df, style)
st.pyplot(fig)
