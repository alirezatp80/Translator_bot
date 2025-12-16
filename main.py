from telebot import TeleBot
from telebot.types import Message
import dotenv , os
from deep_translator import GoogleTranslator
from texts import text
from button import delete_msg
from utility import detect_lang

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start' , 'help' , 'about'])
def Welcome_func(message : Message):
    user_language = 'en'
    
    if user_language == '' :
        pass
    #   set userlanguage
    else:
        if message.text == '/start':
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(message.chat.id ,f'{text[user_language]['welcome']}' )
        if message.text == '/help':
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(message.chat.id ,f'{text[user_language]['help']}',reply_markup=delete_msg() )

        if message.text == '/about':
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(message.chat.id ,f'{text[user_language]['about']}',reply_markup=delete_msg() )

    
@bot.callback_query_handler(func=lambda call : True)
def callback(call):
    if call.data == 'delete_message':
        bot.delete_message(call.message.chat.id , call.message.message_id)
        
@bot.message_handler(func=lambda message :True)
def translate_message(message:Message):
    text = str(message.text)
    # bot.send_message(message.chat.id , 'عاشقتم:)')
    lang = detect_lang(text)
    if lang == 'en' :
        translate = GoogleTranslator(source='en' , target='fa')
        result = translate.translate(text)
    elif lang == 'fa':
        translate = GoogleTranslator(source='fa' , target='en')
        result = translate.translate(text)
    else:
        translate_1 = GoogleTranslator(source='en' , target='fa')
        translate_2 = GoogleTranslator(source='fa' , target='en')
        result = f'{translate_1.translate(text)}\n{translate_2.translate(text)}'
    bot.reply_to(message , result  )
        
    


bot.polling(skip_pending=True)