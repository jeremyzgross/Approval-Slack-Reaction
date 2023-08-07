import requests
from constants import ACCESS_TOKEN
from constants import CHANNEL_ID
from constants import FIRST_MESSAGE_TS

EMOJI = "shrugpool"

# Add emoji reaction
def add_emoji_reaction(message_ts):
    response = requests.post(
        "https://slack.com/api/reactions.add",
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "channel": CHANNEL_ID,
            "timestamp": message_ts,
            "name": EMOJI
        }
    )
    response_data = response.json()
    if response_data.get("ok"):
        print("Emoji reaction added successfully")
    else:
        print("Failed to add emoji reaction:", response_data)

if __name__ == "__main__":
    add_emoji_reaction(FIRST_MESSAGE_TS)
