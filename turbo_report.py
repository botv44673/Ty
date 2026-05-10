import asyncio
import os
from pyrogram import Client
from pyrogram.raw import functions, types

# --- CONFIGURATION ---
API_ID = 24676264  # Apna API ID daalein
API_HASH = "e04ebd801c8ae8b26986c482fb31f853"  # Apna API Hash daalein

# Saare Target Links aur Admin Username
TARGETS = [
    "https://t.me/+6txGkMlASpRiZjBl",
    "https://t.me/+Eh1D10oLzco2MmNl",
    "https://t.me/+wYv4NJXFBk4xYTVl",
    "https://t.me/+x1rDpTIFw_VmODA1",
    "JKVIPOWNER" # Admin ko bhi report karna zaruri hai
]

# Tagda professional message
MESSAGE = (
    "URGENT: This entity is part of a professional fraud syndicate. "
    "They are distributing Trojanized malware (Spyware) disguised as BGMI mods "
    "and selling fake 'Server Freeze' panels. This is a severe violation of "
    "Telegram's Terms of Service regarding fraud and malware distribution. "
    "Please terminate immediately."
)

async def start_reporting(session_file, target):
    session_name = session_file.replace(".session", "")
    async with Client(session_name, API_ID, API_HASH, workdir="./") as app:
        try:
            # Username ya Link dono ko handle karega
            chat = await app.get_chat(target)
            peer = await app.resolve_peer(chat.id)
            
            await app.invoke(
                functions.account.ReportPeer(
                    peer=peer,
                    reason=types.InputReportReasonSpam(),
                    message=MESSAGE
                )
            )
            print(f"[✅] Success: {session_name} -> {target}")
        except Exception as e:
            print(f"[❌] Failed: {session_name} -> {e}")

async def main():
    # Folder mein jitni .session files hain unhe uthana
    sessions = [f for f in os.listdir() if f.endswith(".session")]
    
    if not sessions:
        print("Koi .session file nahi mili! Folder mein sessions rakhein.")
        return

    print(f"🔥 Total {len(sessions)} accounts ke saath attack shuru ho raha hai...")

    for target in TARGETS:
        print(f"\nTargeting: {target}")
        # Saare accounts ko ek saath trigger karna (Parallel)
        tasks = [start_reporting(s, target) for s in sessions]
        await asyncio.gather(*tasks)
        
        # Telegram Flood protection ke liye thoda gap
        print("Wait kar rahe hain agle target ke liye...")
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
