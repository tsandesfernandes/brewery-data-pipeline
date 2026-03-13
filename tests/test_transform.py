import pandas as pd

def test_no_duplicate_ids():

    df = pd.read_json("data/bronze/breweries_raw.json")

    assert df["id"].is_unique