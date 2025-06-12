from discord_webhook import DiscordWebhook, DiscordEmbed

import os
from dotenv import load_dotenv

load_dotenv()
webhook_url = os.getenv("WEBHOOK_TOKEN")

def webhook_embed(title, message_description):
    webhook = DiscordWebhook(url=str(webhook_url))
    embed = DiscordEmbed(title=title, description=message_description)
    webhook.add_embed(embed)
    webhook.execute()
    return