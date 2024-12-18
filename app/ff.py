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
    """
    Filters players by their names.

    Args:
        players (dict): Dictionary of player projections.
        names_to_find (list): List of player names to filter by.

    Returns:
        dict: Filtered players.
    """
    filtered_players = {}
    for player_id, player_info in players.items():
        # Check if 'longName' exists and matches one of the names
        if player_info.get('longName') and player_info['longName'] in names_to_find:
            filtered_players[player_id] = player_info
        elif 'longName' not in player_info:
            print(f"Warning: Missing 'longName' for player ID {player_id}. Skipping.")
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
    try:
        # Ensure the lists have at least one player before accessing them
        if not player_1_projection or not player_2_projection:
            raise IndexError("One of the player projections is empty. Please check the player names or for bye weeks.")

        player_1_points = float(player_1_projection[0]['fantasyPointsDefault'][scoring_format])
        player_2_points = float(player_2_projection[0]['fantasyPointsDefault'][scoring_format])

        # Determine the player with higher fantasy points
        higher_fantasy_player = player_1_projection[0] if player_1_points > player_2_points else player_2_projection[0]

        # Output the player with higher fantasy points
        print("Player with higher fantasy points:", higher_fantasy_player['longName'])
        print("Projected stats:", higher_fantasy_player['fantasyPointsDefault'][scoring_format])
    except IndexError as e:
        print(f"Error: {e}")