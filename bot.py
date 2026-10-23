import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

BOT_TOKEN = "8623415670:AAEWNw0Bqdb78Mh9l3COUpNWD6CznOojm-k"
# Вставьте ссылку с GitHub Pages:
WEB_APP_URL = "https://axenocoder.github.io/book_worm/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📖 Открыть книгу",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])
    await message.answer(
        "👋 **Добро пожаловать в читалку!**\n\n"
        "Нажмите кнопку ниже, чтобы начать чтение книги внутри Telegram:",
        reply_markup=kb,
        parse_mode="Markdown"
    )

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("🚀 Бот запущен! Отправьте ему /start в Telegram")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())