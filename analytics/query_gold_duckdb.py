import duckdb

query = '''
SELECT country, SUM(brewery_count) AS total_breweries
FROM 'data/gold/brewery_aggregates.parquet'
GROUP BY country
ORDER BY total_breweries DESC
'''

print(duckdb.sql(query).df())
