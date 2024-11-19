import requests
import logging
import re
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")


# Helper function to extract emails from text
def extract_emails(text):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


# Function to get Instagram bio based on username
def get_instagram_bio(username):
    """Fetch the Instagram bio of a user (mock example)."""
    # Placeholder URL - Instagram does not allow direct access to bios unless using the Instagram Graph API
    url = f"https://graph.instagram.com/v12.0/{username}?fields=biography&access_token={INSTAGRAM_ACCESS_TOKEN}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return extract_emails(data.get("biography", ""))
    except Exception as e:
        logging.error(f"Error fetching Instagram bio: {e}")
    return []


# Function to get Twitter bio based on username
def get_twitter_bio(username):
    """Fetch the Twitter bio of a user."""
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {"Authorization": f"Bearer {TWITTER_API_KEY}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            bio = data.get("data", {}).get("description", "")
            return extract_emails(bio)
    except Exception as e:
        logging.error(f"Error fetching Twitter bio: {e}")
    return []
