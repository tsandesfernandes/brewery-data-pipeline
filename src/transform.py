import pandas as pd
from pathlib import Path
import shutil

def transform_to_silver():

    bronze_path = "data/bronze/breweries_raw.json"
    silver_path = "data/silver"
    tmp_path = "data/silver_tmp"

    df = pd.read_json(bronze_path)

    df = df.drop_duplicates(subset=["id"])
    df = df.dropna(subset=["country", "state"])

    df["country"] = df["country"].astype(str)
    df["state"] = df["state"].astype(str)
    df["brewery_type"] = df["brewery_type"].astype(str)

    partition_cols = ["country","state"]

    if Path(tmp_path).exists():
        shutil.rmtree(tmp_path)

    df.to_parquet(
        tmp_path,
        engine="pyarrow",
        partition_cols=partition_cols,
        index=False
    )

    if Path(silver_path).exists():
        shutil.rmtree(silver_path)

    shutil.move(tmp_path, silver_path)
