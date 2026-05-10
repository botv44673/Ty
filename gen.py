from pyrogram import Client

# Fresh API Credentials
api_id = 24676264
api_hash = "e04ebd801c8ae8b26986c482fb31f853"

print("--- Telegram Session Generator ---")
name = input("Account ka naam rakhein (e.g. acc1): ")

with Client(name, api_id, api_hash) as app:
    print(f"✅ Session saved as {name}.session")
