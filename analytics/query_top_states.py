import duckdb

query = '''
SELECT country, state, SUM(brewery_count) AS total_breweries
FROM 'data/gold/brewery_aggregates.parquet'
GROUP BY country, state
ORDER BY total_breweries DESC
LIMIT 20
'''

print(duckdb.sql(query).df())
