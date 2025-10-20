
import os
import asyncio
from telegram import Bot
from telegram.ext import ApplicationBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = os.getenv("BOT_TOKEN")

GROUP_IDS = [-1001234567890]  # Grup ID'lerini buraya yaz
MESSAGE = """🎉 ÇEKİLİŞ 🎉
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉

🎉 200 USDT ŞARTLAR 🎉
KANALA KATIL SON PAYLAŞIMA
KALP BIRAK 10 ŞANSLI KİŞİYE 20 
USDT VERİLECEKTİR 
🎉🎉
KANAL: https://t.me/airdropandcrypti
📆 Bitiş süresi:
25/10/2025 00:00"""

async def send_scheduled_message(bot: Bot):
    for gid in GROUP_IDS:
        try:
            await bot.send_message(chat_id=gid, text=MESSAGE)
            print(f"✅ Mesaj gönderildi: {gid}")
        except Exception as e:
            print(f"⚠️ Mesaj gönderilemedi ({gid}): {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    bot = app.bot

    scheduler = AsyncIOScheduler(timezone="Europe/Istanbul")
    # Örneğin her gün saat 21:00'de mesaj at
    scheduler.add_job(send_scheduled_message, "cron", hour=21, minute=0, args=[bot])
    scheduler.start()

    print("🤖 Bot Render üzerinde çalışıyor ve zamanlama aktif...")
    await app.initialize()
    await app.start()
    await asyncio.Event().wait()  # Bot sonsuza kadar açık kalır

if __name__ == "__main__":
    asyncio.run(main())
