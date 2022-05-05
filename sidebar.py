import streamlit as st

def sidebar(shot_df, t1_shot_df, t1_players, t2_shot_df, t2_players):
    shot_df = shot_df
    t1_shot_df = t1_shot_df
    t1_players = t1_players
    t2_shot_df = t2_shot_df
    t2_players = t2_players

    # Select Team or Player
    st.sidebar.header('User Selections')
    level = st.sidebar.selectbox('Choose Level of Analysis', ['Team', 'Player'])
    team = st.sidebar.selectbox("Which Team", (shot_df.TEAM_NAME.unique()[0], shot_df.TEAM_NAME.unique()[1]))

    if level == 'Player':
        if team == shot_df.TEAM_NAME.unique()[0]:
            players = st.sidebar.selectbox("Which Player", t1_players)
        elif team == shot_df.TEAM_NAME.unique()[1]:
            players = st.sidebar.selectbox("Which Player", t2_players)
        return level, team, players
    
    return level, team, None

def styler():
    choice = st.sidebar.selectbox('Choose Style of Shot Chart', ['Hex', 'KDE', 'Contour', 'Scatter'])
    return choice.lower()
