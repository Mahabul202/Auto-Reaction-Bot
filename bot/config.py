from os import environ as env

class Telegram:
    # Use the environment variable if it exists and isn't empty; otherwise, use the default
    _raw_id = env.get("API_ID", "").strip()
    API_ID = int(_raw_id) if _raw_id else 23787292
    
    # Same logic for strings (using 'or' handles empty strings)
    API_HASH = env.get("API_HASH") or "679f843b6d9485bead1b81852a9634f4"
    BOT_TOKEN = env.get("BOT_TOKEN") or "8495938883:AAG0Kiq7MkK4shSLqDJC40rHUpZz9dkOpuo"
    BOT_USERNAME = env.get("BOT_USERNAME") or "Shhs7syshsg_Bot"
    
    EMOJIS = [
        "👍", "👎", "❤", "🔥", "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢", "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡", "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯", "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡", "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡", "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐", "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏", "😘", "👾", "🤷‍♂", "😎"
    ]
    
