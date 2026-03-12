from src.extract import fetch_breweries

def test_fetch():
    data = fetch_breweries()
    assert isinstance(data, list)
