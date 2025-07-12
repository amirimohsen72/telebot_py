
telebot


to access bot api:
````
https://api.telegram.org/bot<token>/METHOD_NAME
````

docoument for read in docs folder.

 auth:
````
 telebot.TeleBot('API_TOKEN_String')
````
 message handler(get) and send messega (send):
 ````
 @bot.message_handler()
def send_wellcome(message):
    if message.text == 'start' :
        bot.send_message(message.chat.id,'خوش آمدید')
````
send file:
````
bot.send_document(message.chat.id,file)
````
reply to message:
````
bot.reply_to(message, 'پیام دریافت شد ')
````


````
bot.send_photo
````
````
bot.send_location(message.chat.id,lat,lon)
````
کانتنت تایپ در مسیج هندلر : نوع پیام دریافتی 
````
@bot.message_handler(content_types=['photo'])
````
برای ذخیره فایل ارسالی کاربر ابتدا اطلاعات فایل مسیر فایل را میده و با فایل دانلود اون را میگیریم و یک فایل خالی با مود wb باز کرده و فایل دانلود را در آن مینویسیم
````
file_info = bot.get_file(message.photo[-1].file_id)
bot.download_file(file_info.file_path)
````
سپس در پایتون فایل دانلود را در یک فایل ذخیره میکنیم.


