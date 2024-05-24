import requests
import time

API_URL = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t="

# List of team names to fetch
team_names = [
    "Arsenal", "Chelsea", "Manchester United", "Liverpool", "Manchester City",
    "Tottenham", "Leicester City", "Everton", "West Ham", "Aston Villa",
    # Add more team names as needed
]

# Rate limit: 100 requests per minute
RATE_LIMIT = 100
TIME_INTERVAL = 60 / RATE_LIMIT

def fetch_team_badge(team_name):
    response = requests.get(API_URL + team_name)
    data = response.json()
    if data['teams']:
        team = data['teams'][0]
        return team['strTeam'], team['strTeamBadge']
    return team_name, None

def main():
    for team_name in team_names:
        team, badge_url = fetch_team_badge(team_name)
        print(f"Team: {team}, Badge URL: {badge_url}")
        time.sleep(TIME_INTERVAL)

if __name__ == "__main__":
    main()
