import requests 
from app.tank01_service import BASE_URL,HEADERS

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

def fetch_team_info(player_name):
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

if __name__ == "__main__":
    fantasy_team={}

    fantasy_team['Quarterback'] = {'name': input("Enter your Quarterback (QB): ")}
    fantasy_team['Running Back 1'] = {'name': input("Enter your first Running Back (RB1): ")}
    fantasy_team['Running Back 2'] = {'name': input("Enter your second Running Back (RB2): ")}
    fantasy_team['Wide Receiver 1'] = {'name': input("Enter your first Wide Receiver (WR1): ")}
    fantasy_team['Wide Receiver 2'] = {'name': input("Enter your second Wide Receiver (WR2): ")}
    fantasy_team['Flex'] = {'name': input("Enter your Flex player: ")}
    fantasy_team['Tight End'] = {'name': input("Enter your Tight End (TE): ")}