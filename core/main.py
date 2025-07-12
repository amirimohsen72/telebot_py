import telebot
import os

dir = os.path.dirname(os.path.abspath(__file__))

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(['command1','command2'])
# @bot.message_handler(content_types=['voice','document','photo'])

@bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')


    elif message.text.startswith('file')  :
        with open('core/testfile.txt','rb') as file:
            bot.send_document(message.chat.id,file)

    else :
        bot.reply_to(message, 'پیام دریافت شد . بعد از بررسی پاسخ خواهیم داد')


bot.infinity_polling()