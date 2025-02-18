from google.cloud import bigquery
import pandas as pd
import os

#Ensure authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/main-crow-418809-888e07ec16c5.json"

#Initialize BigQuery client
client = bigquery.Client()

#Define SQL query
query = """
    SELECT *
    FROM `edhec-business-manageme.luxurydata2502.price-monitoring-2022`
    WHERE currency IN ('USD', 'EUR', 'GBP', 'HKD', 'JPY', 'CHF', 'CNY', 'TWD', 'SGD', 'KRW', 'AED')
"""

#Execute Query
query_job = client.query(query)
df = query_job.to_dataframe()

#Save data locally
df.to_csv("data/raw_price_data.csv", index=False)

print("Data ingestion complete! Saved as 'data/raw_price_data.csv'.")
