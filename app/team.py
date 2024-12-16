import requests 
from os import

def fetch_player_list():
    """
    Fetches the complete list of NFL players.
    """
    url = f"{BASE_URL}/getNFLPlayerList"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching player list: {response.text}")

def search_player_by_name(player_name):
    """
    Searches for a player by name and returns their ID, team, and picture.
    """
    try:
        data = fetch_player_list()  # Fetch the full JSON response
        for player in data['body']:
            if player_name.lower() == player['longName'].lower():
                return {
                    "playerID": player["playerID"],
                    "longName": player["longName"],
                    "team": player["team"],
                    "espnHeadshot": player["espnHeadshot"]
                }
        return None  # Return None if no player matches
    except Exception as e:
        print(f"Error searching for player: {e}")
        return None


# Testing the function
player_name = "Patrick Mahomes"  # Input the player name
player_data = search_player_by_name(player_name)

if player_data:
    print(f"Player Found: {player_data}")
else:
    print("Player not found.")