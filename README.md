# Brewery Data Engineering Pipeline

This project implements a data pipeline that ingests brewery data from the Open Brewery DB API and stores it in a data lake following the **Medallion Architecture**.

Architecture:

API → Bronze → Validation → Silver → Gold → SQL Analytics

## Layers

Bronze
Raw JSON from the API.

Silver
Cleaned Parquet dataset partitioned by country and state.

Gold
Aggregated analytical dataset containing brewery counts by type and location.

## Running the Project

Install dependencies

pip install -r requirements.txt

Start Airflow

docker-compose up --build

Airflow UI

http://localhost:8080

Trigger DAG:

brewery_pipeline

## Query Gold Layer

Install DuckDB

pip install duckdb

Example query:

python analytics/query_gold_duckdb.py

## Tech Stack

Python
Apache Airflow
Pandas
PyArrow
DuckDB
Docker
