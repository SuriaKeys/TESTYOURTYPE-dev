import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

#змінні оточення для токену та Chat ID
TOKEN = os.getenv('7393654949:AAHazwSYZZUd_ntHX_W6n0NoFX9l3nKI7TM')
YOUR_CHAT_ID = os.getenv('1440138507')

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Вітаю я TYT Helper ✋ Якщо у вас є якісь питання, пропозиції або ви найшли баги, пишіть або скидуйте фото/відео у чат😁')

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('💨Ось найбільш поширені запитання та відповіді на них: 1. Я знайшов помилку, що мені робити? -- Ви можете надіслати мені фото/відео з детальним описом, що не так. 2. Як я можу зв\'язатися напряму зі службою підтримки? -- Ви можете залишити повідомлення тут або ж написати розробнику напряму: @wtashame. 3. Чи є можливість брати участь у розробці веб-сайту TestYourType? -- Для цього вам потрібно зв\'язатися з розробником.')

async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Дякую за ваше повідомлення! Зв\'яжемося з вами як найшвидше!💖')

async def handle_photo(update: Update, context: CallbackContext) -> None:
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        photo_file.download('received_photo.jpg')
        await context.bot.send_photo(chat_id=YOUR_CHAT_ID, photo=open('received_photo.jpg', 'rb'))
        await update.message.reply_text("Фото отримано!")

async def handle_video(update: Update, context: CallbackContext) -> None:
    if update.message.video:
        video_file = await update.message.video.get_file()
        video_file.download('received_video.mp4')
        await context.bot.send_video(chat_id=YOUR_CHAT_ID, video=open('received_video.mp4', 'rb'))
        await update.message.reply_text("Відео отримано!")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.VIDEO, handle_video))

    application.run_polling()

if __name__ == '__main__':
    main()
