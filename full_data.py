import requests
import time

# API URLs
ALL_LEAGUES_API_URL = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
LEAGUES_API_URL = "https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l="
BADGE_API_URL = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t="

# Rate limit: 100 requests per minute
RATE_LIMIT = 100
TIME_INTERVAL = 60 / RATE_LIMIT

def fetch_all_leagues():
    try:
        response = requests.get(ALL_LEAGUES_API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        leagues = data.get('leagues', [])
        return leagues
    except Exception as e:
        print(f"Error fetching all leagues: {e}")
        return []

def fetch_teams_from_league(league_name):
    try:
        response = requests.get(LEAGUES_API_URL + league_name.replace(" ", "%20"))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        teams = data.get('teams', [])
        time.sleep(TIME_INTERVAL)  # Respect the rate limit
        return teams
    except Exception as e:
        print(f"Error fetching teams from league {league_name}: {e}")
        return []

def fetch_team_badge(team_name):
    try:
        response = requests.get(BADGE_API_URL + team_name.replace(" ", "%20"))
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if data.get('teams'):
            team = data['teams'][0]
            return team['strTeam'], team['strTeamBadge']
        return team_name, None
    except Exception as e:
        print(f"Error fetching badge for team {team_name}: {e}")
        return team_name, None

def main():
    # Fetch all leagues
    print("Fetching all leagues...")
    leagues = fetch_all_leagues()

    teams_map = {}

    # Fetch teams from each league and store in the dictionary
    for league in leagues:
        league_name = league.get('strLeague')
        print(f"Fetching teams from {league_name}...")
        teams = fetch_teams_from_league(league_name)
        for team in teams:
            team_name = team.get('strTeam')
            teams_map[team_name] = None

    # Fetch badge URLs for each team and print them
    for team_name in teams_map.keys():
        print(f"Fetching badge for team {team_name}...")
        team, badge_url = fetch_team_badge(team_name)
        teams_map[team_name] = badge_url
        print(f"Team: {team}, Badge URL: {badge_url}")
        time.sleep(TIME_INTERVAL)  # Respect the rate limit

if __name__ == "__main__":
    main()
