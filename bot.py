import random
import string
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from config import TELEGRAM_TOKEN, ACCESS_CODE
from browser import ChatGPTBrowser

# Проверка кода доступа
def check_access_code(user_code):
    return user_code == ACCESS_CODE

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Пожалуйста, введите код доступа.")

# Команда /setcode
def set_code(update: Update, context: CallbackContext):
    user_code = ' '.join(context.args)
    if check_access_code(user_code):
        update.message.reply_text("Код доступа принят! Вы можете начать отправлять вопросы.")
        context.user_data['access_granted'] = True
    else:
        update.message.reply_text("Неверный код доступа. Попробуйте снова.")

# Обработка сообщений
def handle_message(update: Update, context: CallbackContext):
    if 'access_granted' not in context.user_data or not context.user_data['access_granted']:
        update.message.reply_text("Для доступа введите правильный код доступа с помощью команды /setcode.")
        return

    # Прокси-сервер (если он требуется, укажите свой сервер)
    proxy = "http://your_proxy:port"  # Замените на ваш прокси

    # Инициализация браузера (ChatGPT через Selenium)
    try:
        chatgpt_browser = ChatGPTBrowser(driver_path="path_to_chromedriver", chatgpt_url="https://chat.openai.com/", proxy=proxy)
        response = chatgpt_browser.send_message(update.message.text)
        update.message.reply_text(response)
    except Exception as e:
        update.message.reply_text(f"Ошибка: {e}")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Регистрируем обработчики
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("setcode", set_code))
    updater.dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()