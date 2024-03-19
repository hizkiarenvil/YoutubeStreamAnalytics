import configparser
import os

# Create a ConfigParser instance
parser = configparser.ConfigParser()

# Read the local config file
# `os.path.join` constructs the path to the config file by joining the directory path of the current file with the relative path to the config file
# __file__ contains the path of the current file
# 'config/config.local' is the relative path to the config file
config_file_path = os.path.join(os.path.dirname(__file__), 'config/config.local')
parser.read(config_file_path)

# Get the YouTube API key and playlist ID from the config file
# These values are expected to be under the section 'youtube' in the config file
YOUTUBE_API_KEY = parser.get('youtube', 'API_KEY')
PLAYLIST_ID = parser.get('youtube', 'PLAYLIST_ID')
