from flask import Flask, request, render_template, Blueprint
from app.team import fetch_team_info

# Define the Blueprint
team_routes = Blueprint("team_route", __name__)

# Team Form Route
@team_routes.route("/team/form", methods=["GET"])
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
        fantasy_team['Quarterback'] = fetch_team_info(request.form.get("QB"))
        fantasy_team['Running Back 1'] = fetch_team_info(request.form.get("RB1"))
        fantasy_team['Running Back 2'] = fetch_team_info(request.form.get("RB2"))
        fantasy_team['Wide Receiver 1'] = fetch_team_info(request.form.get("WR1"))
        fantasy_team['Wide Receiver 2'] = fetch_team_info(request.form.get("WR2"))
        fantasy_team['Tight End'] = fetch_team_info(request.form.get("TE"))
        fantasy_team['Flex'] = fetch_team_info(request.form.get("FLEX"))

        # Pass team data to the display template
        return render_template("team_display.html", team=fantasy_team)
    except Exception as err:
        print('OOPS', err)