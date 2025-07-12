import telebot
import os

dir = os.path.dirname(os.path.abspath(__file__))

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(['action'], func = lambda message:True)
def keyboard_shishee(message):
    markup= telebot.types.InlineKeyboardMarkup()
    button1= telebot.types.InlineKeyboardButton('تلگرام',url='https://t.me/rafanet')
    button2= telebot.types.InlineKeyboardButton(' تکرار (دیتا)نام کالبک',callback_data='testcallback')
    button3= telebot.types.InlineKeyboardButton('سایت',url='https://amirimohsen.ir')
    markup.add(button1)
    markup.add(button2,button3)
    bot.send_message(message.chat.id,'عملیات را انتخاب کنید',reply_markup=markup)
# @bot.message_handler(content_types=['voice','document','photo'])

@bot.callback_query_handler(func=lambda call:True)
def testcallfunction(call):
    if call.data == 'testcallback' :
        bot.send_message(call.message.chat.id,call.data)

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