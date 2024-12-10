# this is the "web_app/routes/ff.py" file ...
url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLProjections"

querystring = {"week":"season","archiveSeason":"2024","twoPointConversions":"2","passYards":".04","passAttempts":"-.5","passTD":"4","passCompletions":"1","passInterceptions":"-2","pointsPerReception":"1","carries":".2","rushYards":".1","rushTD":"6","fumbles":"-2","receivingYards":".1","receivingTD":"6","targets":".1","fgMade":"3","fgMissed":"-1","xpMade":"1","xpMissed":"-1"}


from app.alpha_service import x_rapidapi_key
from app.alpha_service import x_rapidapi_host

headers = {
	"x-rapidapi-key": x_rapidapi_key,
	"x-rapidapi-host": x_rapidapi_host
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

print(data)

player_1 = input("Who is the first player you would like to compare?")
player_2 = input("Who is the second player you would like to compare?")

players = data['body']['playerProjections']

player_1_projection = []
player_2_projection = []

# Function to filter players by longName
def filter_players_by_names(players, names_to_find):
    filtered_players = {}
    for player_id, player_info in players.items():
        if player_info.get('longName') in names_to_find:
            filtered_players[player_id] = player_info
    return filtered_players

# Example: Pull dictionaries for players with the name player_1 or player_2
filtered_players_1 = filter_players_by_names(players, [player_1])
filtered_players_2 = filter_players_by_names(players, [player_2])

# Output the filtered players
player_1_projection = list(filtered_players_1.values())  # Convert to list of player info
player_2_projection = list(filtered_players_2.values())  # Convert to list of player info

# Compare fantasy points (convert to float for proper comparison)
# Assuming there's only one player in each projection list
higher_fantasy_player = player_1_projection[0] if float(player_1_projection[0]['fantasyPoints']) > float(player_2_projection[0]['fantasyPoints']) else player_2_projection[0]

# Output the player with higher fantasy points
print("Player with higher fantasy points:", higher_fantasy_player['longName'])
print("Projected stats:", higher_fantasy_player['fantasyPointsDefault'])