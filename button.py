from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def delete_msg():
    markup = InlineKeyboardMarkup()
    delete_btn = InlineKeyboardButton(' ❌ ' , callback_data='delete_message')
    markup.add(delete_btn)
    return markup