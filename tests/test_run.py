import pytest
from src.menu import ScoreData 

data = ScoreData()

def test_load_data():
    score = data.load()
    assert type(score) == list
    assert len(score) != 0

def test_highest_score():
    hs = data.get_best_score(data.load())
    assert type(hs) == int
    assert hs != 0

