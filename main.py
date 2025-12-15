from telebot import TeleBot
from telebot.types import Message
import dotenv , os
from deep_translator import GoogleTranslator
from texts import text
from button import delete_msg

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
    


bot.polling(skip_pending=True)