from telegram import Bot
from telegram.ext import ApplicationBuilder
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio, os

TOKEN = os.getenv("BOT_TOKEN")

GROUP_IDS = [-1001234567890]  # Grup ID’lerini buraya yaz
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
            print(f"⚠️ {gid} grubuna gönderilemedi: {e}")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    bot = app.bot

    scheduler = BackgroundScheduler(timezone="Europe/Istanbul")
    scheduler.add_job(lambda: asyncio.run(send_scheduled_message(bot)),
                      trigger="cron", hour=22, minute=59)
    scheduler.start()

    print("🤖 Bot Render üzerinde çalışıyor...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
