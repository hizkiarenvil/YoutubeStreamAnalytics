import json
import logging
from pprint import pprint
from kafka import KafkaProducer
import requests

# Importing constants from constants.py
from constants import YOUTUBE_API_KEY, PLAYLIST_ID

# Function to fetch a single page of data from the YouTube API
def fetch_page(url, parameters, page_token=None):
    """
    Fetches a single page of data from the YouTube API.

    Args:
        url (str): The URL of the API endpoint.
        parameters (dict): The parameters to be passed in the request.
        page_token (str, optional): Token for pagination. Defaults to None.

    Returns:
        dict: The JSON response from the API.
    """
    params = {**parameters, 'key': YOUTUBE_API_KEY, 'page_token': page_token}
    response = requests.get(url, params)
    payload = json.loads(response.text)
    return payload

# Generator function to fetch all pages of data from the YouTube API
def fetch_page_lists(url, parameters, page_token=None):
    """
    Generator function to fetch all pages of data from the YouTube API.

    Args:
        url (str): The URL of the API endpoint.
        parameters (dict): The parameters to be passed in the request.
        page_token (str, optional): Token for pagination. Defaults to None.

    Yields:
        dict: Individual items from the API response.
    """
    while True:
        payload = fetch_page(url, parameters, page_token)
        yield from payload['items']
        page_token = payload.get('nextPageToken')
        if page_token is None:
            break

# Function to format the response from the YouTube API
def format_response(video):
    """
    Formats the response from the YouTube API into a standardized format.

    Args:
        video (dict): Video data from the API.

    Returns:
        dict: Formatted video data.
    """
    video_res = {
        'title': video['snippet']['title'],
        'likes': int(video['statistics'].get('likeCount', 0)),
        'comments': int(video['statistics'].get('commentCount', 0)),
        'views': int(video['statistics'].get('viewCount', 0)),
        'favorites': int(video['statistics'].get('favoriteCount', 0)),
        'thumbnail': video['snippet']['thumbnails']['default']['url']
    }
    return video_res

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Fetching videos from a specific playlist
    for video_item in fetch_page_lists(
            "https://www.googleapis.com/youtube/v3/playlistItems",
            {'playlistId': PLAYLIST_ID, 'part': 'snippet,contentDetails'},
            None):
        video_id = video_item['contentDetails']['videoId']

        # Fetching details of each video
        for video in fetch_page_lists(
                "https://www.googleapis.com/youtube/v3/videos",
                {'id': video_id, 'part': 'snippet,statistics'},
                None):
            # Formatting the response and sending it to Kafka
            producer.send('youtube_videos', json.dumps(format_response(video)).encode('utf-8'),
                          key=video_id.encode('utf-8'))
            print('Sent ', video['snippet']['title'])
