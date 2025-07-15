import os
from google.cloud import bigquery
from pandas_processing import df    #pulls clean data from pandas_processing.py

# Authenticate Google Cloud - path to JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/ugoan/Downloads/yt-api-project-465822-5bf4062f9294.json"

# Define BigQuery project, dataset, and table
project_id = 'yt-api-project-465822'
dataset_id = 'youtube_data'
table_id = "channel_stats"

#where to send data
table_ref = f"{project_id}.{dataset_id}.{table_id}"

#connects BigQuery
client = bigquery.Client()

#upload DataFrame to BigQuery
#Every time I load this DataFrame, delete the existing table data and insert this new version
job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")  # overwrite
)
job.result()  #wait for the job to complete

print("DataFrame uploaded successfully.")