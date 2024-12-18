from flask import Flask, request, render_template, Blueprint
from app.team import fetch_player, fetch_player_games
from app.ff import fetch_ff_json
from time import time
import datetime
import json

POSITION_LONG_NAMES = {
    "QB": "Quarterback",
    "RB1": "Running Back 1",
    "RB2": "Running Back 2",
    "WR1": "Wide Receiver 1",
    "WR2": "Wide Receiver 2",
    "TE": "Tight End",
    "FLEX": "Flex"
}

# Define the Blueprint
team_routes = Blueprint("team_route", __name__)

# Team Form Route
@team_routes.route("/team/form")
def team_form():
    print("TEAM INPUT...")
    return render_template("team_form.html")  # Render the input form

# Team View Route
@team_routes.route("/team/view", methods=["GET", "POST"])
def team_view():
    print("TEAM VIEW...")
    try:
        week = request.form.get('week', 1)
        projections: dict = fetch_ff_json(week).get("playerProjections")

        # Fetch player details for each input position
        fantasy_team = {}

        times = []

        for position in POSITION_LONG_NAMES.keys():
            start = time()
            player = request.form.get(position)
            print(player)
            team_info = fetch_player(player)
            fantasy_team[POSITION_LONG_NAMES.get(position)] = team_info
            fantasy_team[POSITION_LONG_NAMES.get(position)]['projections'] = projections.get(team_info['playerID'], {})
            times.append(time() - start)

        print(times)
        print(sum(times) / len(times))

        times = []
        for position, data in fantasy_team.items():
            start = time()
            print(data.get("playerID"))
            games = fetch_player_games(data.get("playerID"))
            parsed_games = []

            for game_id, data in games.items():
                try:
                    year = game_id[0:4]
                    month = game_id[4:6]
                    day = game_id[6:8]
                    game_date = datetime.date(*map(int, [year, month, day]))

                    parsed_games.append((game_date, data))
                except Exception as e:
                    raise Exception(f"Invalid game id: {e}")
                
            fantasy_team[position]['games'] = sorted(parsed_games, key=lambda x: x[0])
            times.append(time() - start)

        print(times)
        print(sum(times) / len(times))

        # Pass team data to the display template
        return render_template("team.html", team=fantasy_team)
    except Exception as err:
        print('OOPS', err)
        return render_template("hello.html")
    
# @team_routes.route("/api/ff/player/<id>", methods=["GET"])
# def ff_player(id):
#     projections = fetch_player_ff(id)
#     return json.dumps(projections)