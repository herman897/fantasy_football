#this is the "test/ff_test.py" file...

from app.ff import fetch_ff_json

def test_ff_data_fetching():

    data = fetch_ff_json(1)
    assert isinstance(data,dict)
    assert len(data['teamDefenseProjections']) == 32
    assert len(data['playerProjections']) > 300

    players = data['playerProjections']
    assert isinstance(players,dict)

    teams = data['teamDefenseProjections']
    assert isinstance(teams,dict)
    