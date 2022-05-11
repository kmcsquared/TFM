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
    mpl.rcParams['font.family'] = 'Avenir'
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.linewidth'] = 2


def get_team_name_from_abbreviation(abbreviation):

    abbreviations_to_name = {
        'ATL': 'Atlanta Hawks',
        'BOS': 'Boston Celtics',
        'CLE': 'Cleveland Cavaliers',
        'CHI': 'Chicago Bulls',
        'DAL': 'Dallas Mavericks',
        'DEN': 'Denver Nuggets',
        'GSW': 'Golden State Warriors',
        'HOU': 'Houston Rockets',
        'LAC': 'Los Angeles Clippers',
        'LAL': 'Los Angeles Lakers',
        'MIA': 'Miami Heat',
        'MIL': 'Milwaukee Bucks',
        'MIN': 'Minnesota Timberwolves',
        'NJN': 'Brooklyn Nets',
        'NYK': 'New York Knicks',
        'ORL': 'Orlando Magic',
        'IND': 'Indiana Pacers',
        'PHI': 'Philadelphia 76ers',
        'PHX': 'Phoenix Suns',
        'POR': 'Portland Trail Blazers',
        'SAC': 'Sacramento Kings',
        'SAS': 'San Antonio Spurs',
        'SEA': 'Oklahoma City Thunder',
        'TOR': 'Toronto Raptors',
        'UTA': 'Utah Jazz',
        'MEM': 'Memphis Grizzlies',
        'WAS': 'Washington Wizards',
        'DET': 'Detroit Pistons',
        'CHH': 'Charlotte Hornets',
        'NOH': 'New Orleans Pelicans',
        'CHA': 'Charlotte Hornets',
        'NOK': 'New Orleans Pelicans',
        'OKC': 'Oklahoma City Thunder',
        'BKN': 'Brooklyn Nets',
        'NOP': 'New Orleans Pelicans'
    }

    return abbreviations_to_name[abbreviation]


def get_team_abbreviation_from_name(name):

    names_to_abbreviation = {
        'Atlanta Hawks': 'ATL',
        'Boston Celtics': 'BOS',
        'Cleveland Cavaliers': 'CLE',
        'Chicago Bulls': 'CHI',
        'Dallas Mavericks': 'DAL',
        'Denver Nuggets': 'DEN',
        'Golden State Warriors': 'GSW',
        'Houston Rockets': 'HOU',
        'Los Angeles Clippers': 'LAC',
        'Los Angeles Lakers': 'LAL',
        'Miami Heat': 'MIA',
        'Milwaukee Bucks': 'MIL',
        'Minnesota Timberwolves': 'MIN',
        'Brooklyn Nets': 'BKN',
        'New York Knicks': 'NYK',
        'Orlando Magic': 'ORL',
        'Indiana Pacers': 'IND',
        'Philadelphia 76ers': 'PHI',
        'Phoenix Suns': 'PHX',
        'Portland Trail Blazers': 'POR',
        'Sacramento Kings': 'SAC',
        'San Antonio Spurs': 'SAS',
        'Oklahoma City Thunder': 'OKC',
        'Toronto Raptors': 'TOR',
        'Utah Jazz': 'UTA',
        'Memphis Grizzlies': 'MEM',
        'Washington Wizards': 'WAS',
        'Detroit Pistons': 'DET',
        'Charlotte Hornets': 'CHA',
        'New Orleans Pelicans': 'NOP'
    }

    return names_to_abbreviation[name]




# https://teamcolorcodes.com/nba-team-color-codes/
NBA_COLORS = {
    'Atlanta Hawks': '#E03A3E',
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
    'Washington Wizards': '#002B5C'
}

