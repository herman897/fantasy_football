#this is the "test/team_test.py" file...

from app.team import fetch_player, fetch_player_games

def test_fetch_player():
    data = fetch_player('Keenan Allen')

    assert isinstance(data,dict)
    assert (data['playerID'] == "15818")
    assert (data['pos'] == "WR")

def test_fetch_player_games():
    data = fetch_player_games('15818')
    # print(data)

    
    assert isinstance(data,dict)
    assert isinstance(data['20241216_CHI@MIN'],dict)
    assert data['20241216_CHI@MIN']['fantasyPointsDefault']['standard']=='14.2'