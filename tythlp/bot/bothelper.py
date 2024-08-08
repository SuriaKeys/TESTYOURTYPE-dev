from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext


TOKEN = "7393654949:AAFGpA-Jv1j3o1xRkKkS7_4KIQ5YQxKW2oE"
YOUR_CHAT_ID = '1440138507'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Вітаю я TYT Helper ✋ Якщо у вас є якісь питання, пропозиції або ви найшли баги, пишіть або скидуйте фото/відео у чат😁')

async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('💨Ось найбільш поширені запитання та відповіді на них: 1. Я знайшов помилку, що мені робити? -- Ви можете надіслати мені фото/відео з детальним описом, що не так. 2. Як я можу зв\'язатися напряму зі службою підтримки? -- Ви можете залишити повідомлення тут або ж написати розробнику напряму: @wtashame. 3. Чи є можливість брати участь у розробці веб-сайту TestYourType? -- Для цього вам потрібно зв\'язатися з розробником.💨')

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    await update.message.reply_text('Дякую за ваше повідомлення! Зв\'яжемося з вами як найшвидше!💖')
    
    
    await context.bot.send_message(chat_id=YOUR_CHAT_ID, text=f"Новий текст від {update.message.from_user.username}: {user_message}")

async def handle_photo(update: Update, context: CallbackContext) -> None:
    if update.message.photo:
        photo_file = await update.message.photo[-1].get_file()
        await photo_file.download_to_drive('received_photo.jpg')

        await update.message.reply_text('Бачу ваше фото. Обов\'язково переглянемо його👍')
        
        
        await context.bot.send_photo(chat_id=YOUR_CHAT_ID, photo=photo_file.file_id)

async def handle_video(update: Update, context: CallbackContext) -> None:
    if update.message.video:
        video_file = await update.message.video.get_file()
        await video_file.download_to_drive('received_video.mp4')
        
        await update.message.reply_text('Бачу ваше відео. Працюю ✅')

        
        await context.bot.send_video(chat_id=YOUR_CHAT_ID, video=video_file.file_id)

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
