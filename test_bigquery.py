from google.cloud import bigquery

try:
    # Initialize the BigQuery client
    client = bigquery.Client()

    # Run a test query
    query = "SELECT 1 AS test_column"
    query_job = client.query(query)  
    results = query_job.result()  

    for row in results:
        print(f"✅ Connection Successful! Test Query Output: {row.test_column}")

except Exception as e:
    print(f"❌ Connection Failed: {e}")
