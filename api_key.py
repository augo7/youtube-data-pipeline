#importing the libraries
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/ugoan/Downloads/yt-api-project-465822-5bf4062f9294.json" #set credentials first
from google.cloud import bigquery 
from googleapiclient.discovery import build #can connect to yt services bc of build function
#Hides API key(key is in .env file)
from dotenv import load_dotenv  
load_dotenv()  
api_key = os.getenv("YOUTUBE_API_KEY")  #get the API key from .env file
youtube = build('youtube', 'v3', developerKey = api_key)


request = youtube.channels().list(
    part = 'statistics',
    forUsername = 'Baxate'
)
response = request.execute()
print(response)

#formatting
channel_stats = response['items'][0]['statistics']      #accessing the statistics part of the response. List accessing synatx  

channel_data = {
    'Channel Name': 'Baxate',                                           #dictionary to store the channel data
    'Subscriber Count': int(channel_stats['subscriberCount']),         #convert from str to int    
    'Total Views': int(channel_stats['viewCount']),
    'Total Videos': int(channel_stats['videoCount'])
}
print(channel_data)

#authenticating google cloud - path to JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/ugoan/Downloads/yt-api-project-465822-5bf4062f9294.json"

client = bigquery.Client()  #allows us to intract with datasets and tables in BigQuery
dataset_id = 'yt-api-project-465822.youtube_data'  #dataset id in BigQuery
table_id = f"{dataset_id}.channel_stats"

schema = [
    bigquery.SchemaField("Channel Name", "STRING", mode = "REQUIRED"),
    bigquery.SchemaField("Subscriber Count", "INTEGER", mode = "REQUIRED"),
    bigquery.SchemaField("Total Views", "INTEGER", mode = "REQUIRED"),
    bigquery.SchemaField("Total Videos", "INTEGER", mode = "REQUIRED")
]

#create/check if table exists
from google.api_core.exceptions import Conflict
table = bigquery.Table(table_id, schema = schema)
try:
    table = client.create_table(table)
    print(f"table {table.project}.{table.dataset_id}.{table.table_id}")
except Conflict:
    print(f"Table {table_id} already exists.")


# insert data into table using batch (free tier safe)
#rows_to_insert = [channel_data]
#errors = client.load_table_from_json(rows_to_insert, table_id).result()
#print("New row has been inserted successfully.")
#commented out when finished so baxate doesnt duplicate
