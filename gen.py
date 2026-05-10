from pyrogram import Client

# Fresh API Credentials
api_id = 23783705
api_hash = "6f809d472288011c75026774e64f77c0"

print("--- Telegram Session Generator ---")
name = input("Account ka naam rakhein (e.g. acc1): ")

with Client(name, api_id, api_hash) as app:
    print(f"✅ Session saved as {name}.session")
