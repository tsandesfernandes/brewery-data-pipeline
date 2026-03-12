FROM python:3.10

WORKDIR /app

ENV AIRFLOW_HOME=/app
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["airflow","standalone"]
