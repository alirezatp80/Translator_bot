from telebot import TeleBot
from telebot.types import Message ,CallbackQuery
import dotenv , os
from deep_translator import GoogleTranslator
from texts import text , alarm_start_bot
from button import delete_msg ,set_lang
from utility import detect_lang ,create_db,insert_user,select_all,select_user , set_language
import time

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)
create_db()
message_delete = {}

@bot.message_handler(commands=['start' , 'help' , 'about','languages'])
def Welcome_func(message : Message):
    
    if message.text == '/start':
        user = select_user(message.from_user.id)
        if not user:
            user = message.from_user
            message_delete['select_language_id']=bot.send_message(message.chat.id , f'{text['en']['languages']}' , reply_markup=set_lang()).id
            bot.delete_message(message.chat.id , message.message_id)
        else:
            bot.send_message(message.chat.id ,f'{text[user[2]]['welcome']}' )
        
        
        
    user = select_user(message.from_user.id)        
            
            
    if message.text == '/help':
        if not user :
            bot.send_message(message.chat.id , alarm_start_bot)
        else:
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(message.chat.id ,f'{text[user[2]]['help']}',reply_markup=delete_msg() )
    if message.text == '/about':
        if not user :
            bot.send_message(message.chat.id , alarm_start_bot)
        else:
            bot.delete_message(message.chat.id , message.message_id)
            bot.send_message(message.chat.id ,f'{text[user[2]]['about']}',reply_markup=delete_msg() )
    if message.text == '/languages':
        if not user :
            bot.send_message(message.chat.id , alarm_start_bot)
        else:
            message_delete['select_language_id']=bot.send_message(message.chat.id , f'{text[user[2]]['languages']}' , reply_markup=set_lang()).id


    
@bot.callback_query_handler(func=lambda call : True)
def callback(call:CallbackQuery):
    if call.data == 'delete_message':
        bot.delete_message(call.message.chat.id , call.message.message_id)
    if call.data == 'set_english_lang':
        user = select_user(call.from_user.id)
        if not user:
            my_user = call.from_user
            insert_user(my_user.id , my_user.username, 'en')
            bot.send_message(call.message.chat.id ,f'{text['en']['welcome']}' )
            
        else:
            bot.send_message(call.message.chat.id ,f'{text['en']['help']}',reply_markup=delete_msg() )
            
            set_language((call.from_user.id) , 'en')  
        bot.delete_message(call.message.chat.id , message_delete['select_language_id'])  
        del message_delete['select_language_id']    
            
        
        
    elif call.data == 'set_farsi_lang':
        user = select_user(call.from_user.id)
        if not user:
            my_user = call.from_user
            insert_user(my_user.id , my_user.username, 'fa')
            bot.send_message(call.message.chat.id ,f'{text['fa']['welcome']}')
        else:
            bot.send_message(call.message.chat.id ,f'{text['fa']['help']}',reply_markup=delete_msg() )
            
            set_language((call.from_user.id) , 'fa')  
        
        bot.delete_message(call.message.chat.id , message_delete['select_language_id'])  
        del message_delete['select_language_id']

        
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