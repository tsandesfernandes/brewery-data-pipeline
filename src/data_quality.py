import pandas as pd

REQUIRED_COLUMNS = ["id","name","brewery_type","country","state"]

def validate_bronze_data(path):

    df = pd.read_json(path)

    if df.empty:
        raise ValueError("Bronze dataset is empty")

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    if not df["id"].is_unique:
        raise ValueError("Duplicate brewery IDs detected")

    print(f"Data quality check passed. Records: {len(df)}")
