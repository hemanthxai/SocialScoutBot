import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    CallbackContext,
)
from utils import get_instagram_bio, get_twitter_bio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Categories for the bot
CATEGORIES = [
    ["Sports", "Music Artists"],
    ["Artists", "Content Creators"],
    ["Movies", "Books"],
    ["Technology", "Gaming"],
    ["Travel", "Food"],
    ["Fitness", "Fashion"],
    ["Education", "Science"],
    ["Business", "Comedy"],
]

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


# Telegram bot handlers
async def start(update: Update, context: CallbackContext):
    """Start the bot and show the category options."""
    keyboard = [
        [InlineKeyboardButton(cat, callback_data=cat) for cat in row]
        for row in CATEGORIES
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Choose a category to search for influencers:",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: CallbackContext):
    """Handle category button click and prompt user for query."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text=f"You selected: {query.data}\nNow send the name of a celebrity or topic."
    )


async def search_influencers(update: Update, context: CallbackContext):
    """Search for influencer bios on Instagram and Twitter."""
    query = update.message.text
    chat_id = update.message.chat_id

    await update.message.reply_text("Searching on Instagram and Twitter...")

    # Instagram Search
    insta_bio = get_instagram_bio(query)

    # Twitter Search
    twitter_bio = get_twitter_bio(query)

    # Combine results
    all_bios = insta_bio + twitter_bio

    if all_bios:
        await update.message.reply_text(
            f"Found the following bios:\n" + "\n".join(all_bios)
        )
    else:
        await update.message.reply_text("No bios found. Try another query or category.")


def main():
    """Set up the bot and start listening for commands."""
    # Create the Application instance
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, search_influencers)
    )

    # Start polling for updates
    application.run_polling()


if __name__ == "__main__":
    main()
