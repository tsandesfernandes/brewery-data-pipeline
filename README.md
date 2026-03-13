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

Use Python 3.10+ and Upgrade pip

pip install --upgrade pip setuptools wheel

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


## Tests

(export PYTHONPATH=$PYTHONPATH:.) if needed

Automated tests using pytest

Data integrity validation in the pipeline

Schema and duplicate validation before Silver transformation


## Monitoring and Alerting

To ensure reliability of the pipeline, monitoring and alerting mechanisms should be implemented to detect pipeline failures, data quality issues, and unexpected changes in the data.

Pipeline Monitoring

The pipeline is orchestrated using Apache Airflow, which provides built-in monitoring features:

DAG execution history

Task-level logs

Task retries

Execution duration metrics

### Failure Alerting

Airflow can be configured to trigger alerts when tasks fail.

Typical alerting strategies include:

#### Email Notifications
#### Messaging Alerts (Slack / Teams)


## Cloud Services Setup

This project runs locally using Docker and Airflow. However, in a production environment it could be deployed using cloud services.

Examples of cloud-based architecture:

API → Airflow → Data Lake (S3) → Data Warehouse → Analytics

Possible cloud components:

Component	Example Services
Object Storage	AWS S3 / Google Cloud Storage / Azure Blob
Orchestration	Airflow (MWAA / Composer / Astronomer)
Data Processing	Spark / Databricks
Analytics	DuckDB / Athena / BigQuery / Snowflake
Example AWS Deployment

A production deployment on AWS could look like:

Open Brewery API
        │
        ▼
AWS MWAA (Managed Airflow)
        │
        ▼
S3 Data Lake
  ├ Bronze
  ├ Silver
  └ Gold
        │
        ▼
Athena / DuckDB / BI Tools