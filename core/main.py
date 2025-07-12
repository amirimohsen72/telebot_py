import telebot
import os
import sqlite3

dir = os.path.dirname(os.path.abspath(__file__))

MAIN_DB = sqlite3.connect('test_db.db',check_same_thread=False)
MAIN_CURSOR = MAIN_DB.cursor()

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(['start'], func = lambda message:True)
def keyboard_keyword(message):
    MAIN_CURSOR.execute("select * from users where chat_id = '"+ str(message.chat.id) +"'")
    result = MAIN_CURSOR.fetchone()
    if result :
        msg = "سلام . خوش آمدی"
    else:
        MAIN_CURSOR.execute("insert into users (chat_id , status) values ('"+ str(message.chat.id) + "','start_0')")
        MAIN_DB.commit()
        msg = 'اولین باره به جمع ما اومدی که !! از حضورت خوش حال شدیم .'

    bot.send_message(message.chat.id,msg)


@bot.message_handler(['action'], func = lambda message:True)
def keyboard_shishee(message):
    markup= telebot.types.InlineKeyboardMarkup()
    button1= telebot.types.InlineKeyboardButton('تلگرام',url='https://t.me/rafanet')
    button2= telebot.types.InlineKeyboardButton(' تکرار (دیتا)نام کالبک',callback_data='testcallback')
    button3= telebot.types.InlineKeyboardButton('سایت',url='https://amirimohsen.ir')
    markup.add(button1)
    markup.add(button2,button3)
    bot.send_message(message.chat.id,'عملیات را انتخاب کنید',reply_markup=markup)


@bot.message_handler(['action2'], func = lambda message:True)
def keyboard_keyword(message):
    # markup= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4,input_field_placeholder='از دکمه کیورد شورتکات انتخاب نمایید', one_time_keyboard=True).add('تست1')
    markup= telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4,input_field_placeholder='از دکمه کیورد شورتکات انتخاب نمایید', one_time_keyboard=True)
    markup.add('حذف کیبورد شورتکات')
    markup.add('نمایش اطلاعات من','متن سوم')
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
    elif message.text == 'حذف کیبورد شورتکات'  :
        bot.send_message(message.chat.id,'شروع مجدد', reply_markup=telebot.types.ReplyKeyboardRemove())
    
    elif message.text == 'نمایش اطلاعات من'  :
        MAIN_CURSOR.execute("select * from users where chat_id='"+str(message.chat.id)+"'")
        result = MAIN_CURSOR.fetchone()
        bot.send_message(message.chat.id, f'''
🔰 اطلاعات
    سن شما ```{result[1]}```
    نام شما ```{result[2]}```
    نام خانوادگی شما ```{result[3]}```
⚡🎃
''', parse_mode='Markdown')
        # jsdc = str(user[2] + ' ' + ' status :' + user[4])
        # bot.send_message(message.chat.id,jsdc)

    elif message.text.startswith('file')  :
        with open('core/testfile.txt','rb') as file:
            bot.send_document(message.chat.id,file)

    else :
        bot.reply_to(message, 'پیام دریافت شد . بعد از بررسی پاسخ خواهیم داد')


bot.infinity_polling()