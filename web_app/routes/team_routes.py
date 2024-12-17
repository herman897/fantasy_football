from flask import Flask, request, render_template, Blueprint
from app.team import fetch_team_info, fetch_player_ff
from time import time
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
        # Fetch player details for each input position
        fantasy_team = {}

        times = []

        for position in POSITION_LONG_NAMES.keys():
            start = time()
            player = request.form.get(position)
            print(player)
            team_info = fetch_team_info(player)
            fantasy_team[POSITION_LONG_NAMES.get(position)] = team_info
            fantasy_team[POSITION_LONG_NAMES.get(position)]['projections'] = fetch_player_ff(team_info['playerID'])

            print(fantasy_team[POSITION_LONG_NAMES.get(position)]['projections'])
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