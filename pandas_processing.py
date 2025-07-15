import os
import pandas as pd
from googleapiclient.discovery import build

from dotenv import load_dotenv  
load_dotenv()  
api_key = os.getenv("YOUTUBE_API_KEY")  
youtube = build('youtube', 'v3', developerKey = api_key)

channels = ['Baxate', 'Vsauce', 'RDCworld1', 'NFL']
all_channel_data = []

for username in channels:
    request = youtube.channels().list(
        part = 'statistics',
        forUsername = username        
    )
    response = request.execute()

    if 'items' not in response or not response['items']:
        print(f"No data found for: {username}")
        continue

    stats = response['items'][0]['statistics']

    #raw data from YT API as python dictionary
    channel_data = {
        'Channel Name': username,
        'Subscriber Count': int(stats['subscriberCount']),
        'Total Views': int(stats['viewCount']),
        'Total Videos': int(stats['videoCount'])
    }

    all_channel_data.append(channel_data)

#create a DataFrame w/ one row from dictionary
df = pd.DataFrame(all_channel_data)
print(df)

if __name__ == '__main__':
    print("Transform complete.")