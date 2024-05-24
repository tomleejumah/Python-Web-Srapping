import requests

# API URL
ALL_LEAGUES_API_URL = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"

def fetch_all_leagues():
    response = requests.get(ALL_LEAGUES_API_URL)
    data = response.json()
    leagues = data.get('leagues', [])
    return leagues

def main():
    # Fetch all leagues
    print("Fetching all leagues...")
    leagues = fetch_all_leagues()

    # Print the league names
    for league in leagues:
        league_name = league.get('strLeague')
        print(f"League: {league_name}")

if __name__ == "__main__":
    main()
