# SocialScoutBot

SocialScoutBot is a Telegram bot that helps users search for influencers across social media platforms like Instagram and Twitter. The bot allows users to search for public profiles, extract emails from bios (where available), and view the results directly in Telegram.

You can access the bot here: [SocialScoutBot](https://t.me/Social_Scout_Bot)

## Features

- Search for influencers by category (e.g., Sports, Music, Movies, etc.).
- Extract emails from Instagram and Twitter bios (when available).
- Display search results directly in Telegram.

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.x installed.
- A Telegram bot token (create a bot on Telegram by talking to [@BotFather](https://core.telegram.org/bots#botfather)).
- API keys for Instagram and Twitter (if you plan to use those platforms for searching).

## How to Use the Bot

### Start the Bot:
1. Open the Telegram app and search for [SocialScoutBot](https://t.me/Social_Scout_Bot).
2. Click on **Start** to begin interacting with the bot.

### Choose a Category:
1. The bot will prompt you to select a category from a list (e.g., Sports, Music, Movies, etc.).
2. Click on a category to proceed.

### Search for an Influencer:
1. After selecting a category, the bot will ask you to send the name of a celebrity or topic (e.g., "Cristiano Ronaldo", "Taylor Swift").
2. The bot will search Instagram and Twitter for profiles related to the name you provide.

### View Results:
1. The bot will display any emails it finds in the bios of matching Instagram or Twitter profiles.
2. If no emails are found, the bot will prompt you to try another query.

## Code Structure

- **bot.py**: Main bot logic, handling commands and interactions with the Telegram API.
- **utils.py**: Helper functions for scraping social media profiles and extracting emails.
- **.env**: Stores your API keys and tokens (never share this file).
- **requirements.txt**: Lists the required Python packages.
