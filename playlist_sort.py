import requests
import pandas as pd
import colorama
import datetime
import random

def get_path():
    def safe_chdir(path):
        try:
            os.chdir(path)
        except UnicodeEncodeError:
            encoded_path = path.encode('utf-8').decode('utf-8')
            os.chdir(encoded_path)

    if getattr(sys, 'frozen', False):
        safe_chdir(os.path.dirname(sys.executable))
    else:
        safe_chdir(os.path.dirname(os.path.abspath(__file__)))
    cwd = os.getcwd()
    return cwd

API_KEY = 'YOUR-API-KEY-HERE'
PLAYLIST_ID = 'YOUR-PLAYLIST-ID-HERE'

time = datetime.datetime.now()
time = time.strftime("%d_%m_%Y_%H-%M-%S")
cwd = get_path()

def get_playlist_items(api_key, playlist_id):
    url = f'https://www.googleapis.com/youtube/v3/playlistItems'
    params = {
        'part': 'snippet',
        'playlistId': playlist_id,
        'maxResults': 50,
        'key': api_key
    }

    items = []
    while True:
        response = requests.get(url, params=params)
        data = response.json()

        items.extend(data.get('items', []))

        if 'nextPageToken' not in data:
            break
        params['pageToken'] = data['nextPageToken']

    return items


def extract_video_info(items):
    videos = []
    for item in items:
        title = item['snippet']['title']
        video_id = item['snippet']['resourceId']['videoId']

        if " - " in title:
            artist = title.split(" - ")[0].strip()
        elif "|" in title:
            artist = title.split("|")[0].strip()
        else:
            artist = item['snippet']['videoOwnerChannelTitle']

        videos.append({
            'title': title,
            'video_id': video_id,
            'artist': artist
        })

    return videos
def save_sorted_videos(videos):
    if not videos:
        print("Warning: 'videos' list is empty.")
        return

    df = pd.DataFrame(videos)
    print("DataFrame columns:", df.columns)

    if 'artist' not in df.columns:
        print("Error: 'artist' column is missing.")
        return

    df_sorted = df.sort_values(by='artist')
    df_sorted.to_csv(f'sorted_playlist_{time}.csv', index=False)
    print(f"{colorama.Fore.LIGHTGREEN_EX}'sorted_playlist_{time}.csv' file saved succesfully to {cwd}")

items = get_playlist_items(API_KEY, PLAYLIST_ID)
videos = extract_video_info(items)
save_sorted_videos(videos)