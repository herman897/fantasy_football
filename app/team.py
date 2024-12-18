import requests 
from app.tank01_service import BASE_URL,HEADERS

# def fetch_player_list():
#     """
#     Fetches the complete list of NFL players.
#     """
#     url = f"{BASE_URL}/getNFLPlayerList"
#     response = requests.get(url, headers=HEADERS)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error fetching player list: {response.text}")

def fetch_player(name):
    """
    Fetches a player and relevant information from the PLayer Info endpoint.

    args:
        name (str): The player's name
    
    Returns:
        dict: Relevant player info for dashboard (team, picture) and fetches to other endpoints (player ID) 
    """
    url = f"{BASE_URL}/getNFLPlayerInfo?playerName={name}&getStats=true"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json().get("body")[0]
    else:
        raise Exception(f"Error fetching player: {response.text}")


# Consolidated into fetch_player:
# def fetch_team_info(player_name):
#     """
#     Searches for a player by name and returns their ID, team, and picture.
#     """
#     try:
#         data = fetch_player(player_name)
#         return data[0]
#     except Exception as e:
#         print(f"Error searching for player: {e}")
#         return None

# def fetch_player_ff(player_id):
#     url = f"{BASE_URL}/getNFLProjections?playerID={player_id}"
#     response = requests.get(url, headers=HEADERS)

#     if response.status_code == 200:
#         return response.json()['body']
#     else:
#         raise Exception(f"Error fetching player: {player_id}")

def fetch_player_games(player_id):
    """
    Fetches a player's recent game's using their player ID.

    args:
        name (str): The player's id
    
    Returns:
        dict: Info on recent games (which includes fantasy scoring for graph) 
    """
    url = f"{BASE_URL}/getNFLGamesForPlayer?playerID={player_id}&fantasyPoints=true"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json().get("body")
    else:
        raise Exception(f"Error fetching game info for player {player_id}")

if __name__ == "__main__":
    fantasy_team={}