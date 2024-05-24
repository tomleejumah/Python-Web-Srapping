import requests
import time

# API URLs
LEAGUES_API_URL = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l="
BADGE_API_URL = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t="

# List of leagues to fetch teams from
# LEAGUES = [
#     "English Premier League", "Spanish La Liga", "Italian Serie A", 
#     "French Ligue 1", "German Bundesliga", "Dutch Eredivisie", 
#     "Portuguese Primeira Liga", "Belgian Jupiler Pro League", 
#     "Russian Premier League", "Turkish Super Lig"
# ]

LEAGUES = [
    "English Premier League", "English League Championship", "Scottish Premier League",
    "German Bundesliga", "Italian Serie A", "French Ligue 1", "Spanish La Liga",
    "Greek Superleague Greece", "Dutch Eredivisie", "Belgian Pro League", "Turkish Super Lig",
    "Danish Superliga", "Portuguese Primeira Liga", "American Major League Soccer",
    "Swedish Allsvenskan", "Mexican Primera League", "Brazilian Serie A", "Ukrainian Premier League",
    "Russian Football Premier League", "Australian A-League", "Norwegian Eliteserien",
    "Chinese Super League", "_No League", "Formula 1", "Formula E", "BTCC", "IndyCar Series",
    "NHL", "UK Elite Ice Hockey League", "NBA", "NBA G League", "NFL", "NASCAR Cup Series",
    "Italian Serie B", "Scottish Championship", "English League 1", "English League 2",
    "Italian Serie C Girone C", "German 2. Bundesliga", "Spanish La Liga 2", "French Ligue 2",
    "Swedish Superettan", "Brazilian Serie B", "CFL", "Argentinian Primera Division",
    "MotoGP", "Spanish Liga ACB", "WRC", "British GT Championship", "WTCC"
]


# Rate limit: 100 requests per minute
RATE_LIMIT = 100
TIME_INTERVAL = 60 / RATE_LIMIT

def fetch_teams_from_league(league_name):
    response = requests.get(LEAGUES_API_URL + league_name.replace(" ", "%20"))
    data = response.json()
    teams = data.get('teams', [])
    return teams

def fetch_team_badge(team_name):
    response = requests.get(BADGE_API_URL + team_name.replace(" ", "%20"))
    data = response.json()
    if data['teams']:
        team = data['teams'][0]
        return team['strTeam'], team['strTeamBadge']
    return team_name, None

def main():
    teams_map = {}

    # Fetch teams from all leagues and store in the dictionary
    for league in LEAGUES:
        teams = fetch_teams_from_league(league)
        for team in teams:
            team_name = team.get('strTeam')
            teams_map[team_name] = None

    # Fetch badge URLs for each team and print them
    for team_name in teams_map.keys():
        team, badge_url = fetch_team_badge(team_name)
        teams_map[team_name] = badge_url
        print(f"Team: {team}, Badge URL: {badge_url}")
        time.sleep(TIME_INTERVAL)

if __name__ == "__main__":
    main()
