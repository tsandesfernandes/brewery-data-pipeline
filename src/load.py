import glob
import pandas as pd
from pathlib import Path

def create_gold_layer():

    files = glob.glob("data/silver/*/*/*.parquet")

    dfs = []

    for f in files:
        try:
            df = pd.read_parquet(f)

            parts = Path(f).parts

            country = [p for p in parts if p.startswith("country=")][0].split("=")[1]
            state = [p for p in parts if p.startswith("state=")][0].split("=")[1]

            df["country"] = country
            df["state"] = state

            dfs.append(df)

        except Exception as e:
            print(f"Skipping corrupted file: {f}", e)

    if not dfs:
        raise ValueError("No valid parquet files found in Silver layer")

    df = pd.concat(dfs, ignore_index=True)

    agg = (
        df.groupby(["country","state","brewery_type"])
        .size()
        .reset_index(name="brewery_count")
    )

    Path("data/gold").mkdir(parents=True, exist_ok=True)

    agg.to_parquet("data/gold/brewery_aggregates.parquet", index=False)
