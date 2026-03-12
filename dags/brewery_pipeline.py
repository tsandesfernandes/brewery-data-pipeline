from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from src.extract import fetch_breweries, save_raw
from src.data_quality import validate_bronze_data
from src.transform import transform_to_silver
from src.load import create_gold_layer


def extract_and_save():
    data = fetch_breweries()
    save_raw(data)


default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="brewery_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
) as dag:

    extract = PythonOperator(
        task_id="extract_api",
        python_callable=extract_and_save,
    )

    validate = PythonOperator(
        task_id="validate_bronze",
        python_callable=validate_bronze_data,
        op_args=["data/bronze/breweries_raw.json"]
    )

    silver = PythonOperator(
        task_id="create_silver",
        python_callable=transform_to_silver,
    )

    gold = PythonOperator(
        task_id="create_gold",
        python_callable=create_gold_layer,
    )

    extract >> validate >> silver >> gold
