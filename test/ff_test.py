#this is the "test/ff_test.py" file...

from app.ff import fetch_ff_json

def test_ff_data_fetching():

    data = fetch_ff_json(1)
    assert isinstance(data,dict)
    assert len(data['body']['teamDefenseProjections']) == 32
    assert len(data['body']['playerProjections']) > 300

    players = data['body']['playerProjections']
    assert isinstance(players,dict)

    teams = data['body']['teamDefenseProjections']
    assert isinstance(teams,dict)
    