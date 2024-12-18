# this is the "app/ff.py" file ...

import requests 
from app.tank01_service import BASE_URL,HEADERS


def fetch_ff_json(week_number):
    """
    Fetches a player's fantasy projection for a given week.

    args:
        name (str): The requested week
    
    Returns:
        dict: All player projections for a given week 
    """
    url = f"{BASE_URL}/getNFLProjections"
    querystring = {"week":week_number,"archiveSeason":"2024"}

    response = requests.get(url, headers=HEADERS, params=querystring)

    if response.status_code == 200:
        return response.json().get("body")

    raise Exception("Failed to fetch fantasy projections")


def filter_players_by_names(players, names_to_find):
    filtered_players = {}
    for player_id, player_info in players.items():
        if player_info.get('longName') in names_to_find:
            filtered_players[player_id] = player_info
    return filtered_players


if __name__ == "__main__":
    
    week_number = input("Enter week number for comparison (or enter anything for full 2024 season projections): ")
    
    scoring_format=""
    options=['standard','PPR', 'halfPPR']
    while scoring_format not in options:
        scoring_format = input("Input your league scoring format ('standard','PPR', or 'halfPPR'): ")
        if scoring_format not in options:
            print("Please input a valid scoring format:")
    
    player_1 = input("Who is the first player you would like to compare? ")
    player_2 = input("Who is the second player you would like to compare? ")

    data = fetch_ff_json(week_number)

    players = data['playerProjections']

    player_1_projection = []
    player_2_projection = []

    # Example: Pull dictionaries for players with the name player_1 or player_2
    filtered_players_1 = filter_players_by_names(players, [player_1])
    filtered_players_2 = filter_players_by_names(players, [player_2])

    # Output the filtered players
    player_1_projection = list(filtered_players_1.values())  # Convert to list of player info
    player_2_projection = list(filtered_players_2.values())  # Convert to list of player info

    # Compare fantasy points (convert to float for proper comparison)
    # Assuming there's only one player in each projection list
    higher_fantasy_player = player_1_projection[0] if float(player_1_projection[0]['fantasyPointsDefault'][scoring_format]) > float(player_2_projection[0]['fantasyPointsDefault'][scoring_format]) else player_2_projection[0]

    # Output the player with higher fantasy points
    print("Player with higher fantasy points:", higher_fantasy_player['longName'])
    print("Projected stats:", higher_fantasy_player['fantasyPointsDefault'][scoring_format])