import os
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

# Function to draw basketball court
def create_court(ax, color):
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)

    # 3PT arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))

    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))

    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))
    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
        
    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)

    # General plot parameters
    # mpl.rcParams['font.family'] = 'Avenir'
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.linewidth'] = 2


def team_data_graph(team1: pd.DataFrame, team2: pd.DataFrame):
    """Métricas de dos queipos.

    Args:
        team1 (pd.DataFrame): Datos del equipo 1 (columna derecha)
        team2 (pd.DataFrame): Datos del equipo 2 (columna izquierda)
    """
    total_tiros = len(team1['PLAYER_NAME'])
    total_jugadores = len(team1['PLAYER_NAME'].unique())
    tiros_2pt = len(team1[team1['SHOT_TYPE'] == '2PT Field Goal'])
    tiros_3pt = len(team1[team1['SHOT_TYPE'] == '3PT Field Goal'])

    total_tiros_2= len(team2['PLAYER_NAME'])
    total_jugadores_2 = len(team2['PLAYER_NAME'].unique())
    tiros_2pt_2 = len(team2[team2['SHOT_TYPE'] == '2PT Field Goal'])
    tiros_3pt_2 = len(team2[team2['SHOT_TYPE'] == '3PT Field Goal'])


    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = st.columns(10)

    with c2:
        st.metric(label = 'Tiros realizados', value = total_tiros)
    with c3:
        st.metric(label = 'Tiros de 2PT', value = tiros_2pt)
    with c4:
        st.metric(label = 'Tiros de 3PT', value = tiros_3pt)
    with c5:
        st.metric(label = 'Jugadores', value = total_jugadores)

    with c7:
        st.metric(label = 'Tiros realizados', value = total_tiros_2)
    with c8:
        st.metric(label = 'Tiros de 2PT', value = tiros_2pt_2)
    with c9:
        st.metric(label = 'Tiros de 3PT', value = tiros_3pt_2)
    with c10:
        st.metric(label = 'Jugadores', value = total_jugadores_2)

def get_shot_percentages(df):

    all_shots_percentage = round(100*sum(df['SHOT_MADE_FLAG']) / len(df), 2)
    two_pts = df[df['SHOT_TYPE'] == '2PT Field Goal']
    two_pt_percentage = round(100*sum(two_pts['SHOT_MADE_FLAG']) / len(two_pts), 2)
    three_pts = df[df['SHOT_TYPE'] == '3PT Field Goal']
    three_pt_percentage = round(100*sum(three_pts['SHOT_MADE_FLAG']) / len(three_pts), 2)

    return [all_shots_percentage, two_pt_percentage, three_pt_percentage]

# https://teamcolorcodes.com/nba-team-color-codes/
NBA_COLORS = {'Atlanta Hawks': '#E03A3E',
              'Boston Celtics': '#007A33',
              'Brooklyn Nets': '#000000',
              'Charlotte Hornets': '#1D1160',
              'Chicago Bulls': '#CE1141',
              'Cleveland Cavaliers': '#860038',
              'Dallas Mavericks': '#00538C',
              'Denver Nuggets': '#0E2240',
              'Detroit Pistons': '#C8102E',
              'Golden State Warriors': '#1D428A',
              'Houston Rockets': '#CE1141',
              'Indiana Pacers': '#002D62',
              'LA Clippers': '#C8102E',
              'Los Angeles Lakers': '#552583',
              'Memphis Grizzlies': '#5D76A9',
              'Miami Heat': '#98002E',
              'Milwaukee Bucks': '#00471B',
              'Minnesota Timberwolves': '#0C2340',
              'New Orleans Pelicans': '#0C2340',
              'New York Knicks': '#006BB6',
              'Oklahoma City Thunder': '#007AC1',
              'Orlando Magic': '#0077C0',
              'Philadelphia 76ers': '#006BB6',
              'Phoenix Suns': '#1D1160',
              'Portland Trail Blazers': '#E03A3E',
              'Sacramento Kings': '#5A2D81',
              'San Antonio Spurs': '#C4CED4',
              'Toronto Raptors': '#CE1141',
              'Utah Jazz': '#002B5C',
              'Washington Wizards': '#002B5C'}


def draw_league_team_comparison(percentages, team):

        X = np.arange(3)
        fig = plt.figure(figsize=(2.5, 2))
        ax4 = fig.add_axes([0,0,1,1])
        ax4.bar(X, percentages[0], color = '#B4975A', width = 0.25)
        ax4.bar(X + 0.25, percentages[1], color = NBA_COLORS[team], width = 0.25)
        
        ax4.set_ylabel('Porcentaje de Acierto (%)', fontsize=10)
        ax4.tick_params(axis='y', which='major', labelsize=10)
        ax4.legend(labels=['Resto de la Liga', team], prop={'size': 4.5})
        ax4.set_xticks(X+0.125)
        ax4.set_xticklabels(['Tiros de Campo', 'Tiros de 2', 'Tiros de 3'], fontsize=8)
        # ax4.set_yticks(np.arange(0, 65, 10), fontsize=4)

        ax4.bar_label(ax4.containers[0], fontsize=4, padding=-10, color='white', weight='bold')
        ax4.bar_label(ax4.containers[1], fontsize=4, padding=-10, color='white', weight='bold')

        st.pyplot(fig=fig)